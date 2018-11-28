from __future__ import print_function
from multiprocessing import Pool, Manager
from os import getpid
from sys import argv, stderr
from time import strftime
from sys import version_info
from getopt import getopt, GetoptError

if version_info[0] < 3:
    range = xrange


def multicase(input_list):
    [case_number, case, solver, queue] = input_list
    queue.put([getpid(), 0, case_number])
    answer = solver(case)
    queue.put([getpid(), 1, case_number, answer])


class FileWrapper(object):
    def __init__(self, file):
        self.file = file
    
    def get_int(self):
        return int(self.file.readline())
    
    def get_ints(self):
        return [int(z) for z in self.file.readline().split()]
    
    def get_float(self):
        return float(self.file.readline())
    
    def get_floats(self):
        return [float(z) for z in self.file.readline().split()]
    
    def get_words(self):
        return self.file.readline().split()
    
    def readline(self):
        return self.file.readline().strip()
    
    def close(self):
        self.file.close


class GCJ(object):
    """
    Wrapper for a lot of functionality that is useful when trying to solve a 
    Google Code jam question.

    For the case of Problem A of the 2008 Qualification Round, example code
    would be:

    def parse(inFile):
        N = int(inFile.readline())
        searchEngines = [inFile.readline().strip() for z in xrange(N)]
        Q = int(inFile.readline())
        queries = [inFile.readline().strip() for z in xrange(Q)]
        return [searchEngines, queries]

    def solve([searchEngines, queries]):
        N = len(searchEngines)
        dict = {searchEngines[i]: i for i in xrange(N)}
        qs = [dict[k] for k in queries]
        used = [False] * N
        numberused = 0
        resets = 0
        for k in qs:
            if not used[k]:
               if numberused == N - 1:
                  resets += 1
                  numberused = 0
                  used = [False] * N
               used[k] = True
               numberused += 1
        return str(resets)

    if __name__ == "__main__":
        from GCJ import GCJ
        GCJ(parse, solve, "c:\\temp", "a").run()

    This would give a script with command line options -t, -s, -l, -r, -v, -m:
      -t (default)
        input file  = "c:\\temp\\a-test.in"
        output file = "c:\\temp\\a-test.out"
        error file  = "c:\\temp\\a-test.err"
        (the directory "c:\\temp" and the character "a" at the start of the
         filenames come from arguments to GCJ in the source code)
      -s <number>
        input file  = "c:\\temp\\a-small-attempt<number>.in"
        output file = "c:\\temp\\a-small-attempt<number>.out"
        error file  = "c:\\temp\\a-small-attempt<number>.err"
      -l
        input file  = "c:\\temp\\a-large.in"
        output file = "c:\\temp\\a-large.out"
        error file  = "c:\\temp\\a-large.err"
      -r (default)
        read the input file. Read the first line to get the number of cases N
        included in the input. Run parse(infile) N times to get N case objects,
        and then run solve(case object) on each of them. Output the strings
        returned from solve, prepended with "Case #<case #>: ". Put output in 
        output file, overwriting it if it exists.
      -v
        Do the same as above, but check if the contents of the output file now
        are as they would be otherwise. If it is, say "OK". Otherwise, output all
        differences, and write the output into the error file, overwriting it if
        it exists.
      -m <number>
        Set up a pool of <number> worker threads, and put all of the problems
        (along with their problem numbers) on a queue. Each thread, when finished
        with a problem, will take the next case from the queue.
"""

    def __init__(self, reader, solver, directory, question):
        self.reader = reader
        self.solver = solver
        self.question = question
        print("GCJ Wrapper initiated.", file=stderr)
        print("Reading command line arguments", file=stderr)
        try:
            opts, args = getopt(argv[1:],
                                "vs:tlm:",
                                ["validate", "small", "test", "large", "multi"])
        except GetoptError as err:
            print(str(err))
            exit(2)
        data_type = "test"
        self.job = "run"
        self.multi = 1
        for o,a in opts:
            if o in ("-s", "--small"):
                data_type = "small-1-attempt" + str(int(a))
            elif o in ("-l", "--large"):
                data_type = "large"
            elif o in ("-v", "--validate"):
                self.job = "validate"
            elif o in ("-m", "--multi"):
                self.multi = int(a)
        file_preface = directory + "/" + question + "-" + data_type
        self.infile = file_preface + ".in"
        self.outfile = file_preface + ".out"
        self.errfile = file_preface + ".err"
        if self.job == "run":
            print("Creating " + self.outfile + " from " + self.infile, file=stderr)
        else:
            print("Testing that " + self.outfile + " would create " + self.infile, file=stderr)
            print("Storing output in " + self.errfile + " otherwise", file=stderr)
            
    def run(self):
        data = self.read()
        if self.multi == 1:
            answers = self.process(data)
        else:
            answers = self.multiprocess(data, self.multi)
        text = "".join(["Case #%d: %s\n" % (k + 1, answers[k]) for k in range(len(answers))])
        if False:
            print(text)
        self.output(text)
        
    def read(self):
        inh = FileWrapper(open(self.infile, 'r'))
        N = inh.get_int()
        data = [self.reader(inh) for _ in range(N)]
        inh.close()
        return data
    
    def process(self, data):
        N = len(data)
        answers = [None] * N
        for k in range(N):
            print("%s:Working on Case %d" % (strftime("%X"), k + 1))
            answers[k] = self.solver(data[k])
            print("%s:Dealt with Case %d: %s" % (strftime("%X"), k + 1, answers[k]))
        return answers
    
    def multiprocess(self, data, num_procs):
        N = len(data)
        manager = Manager()
        queue = manager.Queue()
        data = [[k + 1, data[k], self.solver, queue] for k in range(N)]
        pool = Pool(num_procs)
        pool.map_async(multicase, data, 1)
        answers = [None] * N
        worker_pids = []
        working_on = []
        num_todo = N
        num_doing = 0
        num_done = 0
        for k in range(2 * N):
            report = queue.get()
            pid = report[0]
            if pid in worker_pids:
                idx = worker_pids.index(pid)
            else:
                idx = len(worker_pids)
                worker_pids += [pid]
                working_on += [None]
            if report[1] == 0:
                working_on[idx] = report[2]
                num_todo -= 1
                num_doing += 1
            else:
                working_on[idx] = None
                answers[report[2] - 1] = report[3]
                num_doing -= 1
                num_done += 1
            print("%s:num_done %s, num_doing %s, num_todo %s | %s" % (strftime("%X"), self.clean(num_done), self.clean(num_doing),
                                                      self.clean(num_todo), " ".join([self.clean(z) for z in working_on])))
        return answers
    
    def output(self, text):
        if self.job == "run":
            open(self.outfile, 'w').write(text)
        else:
            text2 = open(self.outfile, 'r').read()
            if text.strip() == text2.strip():
                print("OK")
            else:
                print("Not OK")
                open(self.errfile, 'w').write(text)
                print("new output written to %s" % self.errfile)
                print("Differences:")
                text = text.strip().split("\n")
                text2 = text2.strip().split("\n")
                for k in range(min(len(text), len(text2))):
                    if text[k] != text2[k]:
                        print("Line %d: '%s' vs '%s'" % (k + 1, text[k], text2[k]))
                if len(text) != len(text2):
                    print("Files have different number of lines: %d vs %d" % (len(text), len(text2)))

    @staticmethod
    def clean(r):
        return "   " if (r is None) else ("%3d" % r)
