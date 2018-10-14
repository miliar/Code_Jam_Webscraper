import os, sys, time, math

class MyPerf:
    def __init__(self, onoff = True):
        if onoff == True:
            self.CHECK_PERF = onoff
        else:
            self.CHECK_PERF = False
        self.PERF = {}

    def timing_start(self, timing_key):
        self.PERF[timing_key] = time.clock()

    def timing_end(self, timing_key):
        result = 0
        if self.PERF.has_key(timing_key):
            time_now = time.clock()
            result = time_now - self.PERF[timing_key]

        if self.CHECK_PERF:
            print "{0} took {1} seconds".format(timing_key, result)

        return result
    
    def set_check_perf(self, onoff):
        if onoff == True:
            self.CHECK_PERF = onoff
        else:
            self.CHECK_PERF = False


class MySolution:
    MAX_T = 100
    MAX_S = 1000
    MAX_K = MAX_S

    def __init__(self, inpf, outf = None):
        self.inputf = open(inpf, 'r')
        self.numcases = int(self.inputf.readline())
        #self.debug = True 
        self.debug = False 

    def print_error(self, name):
        print "ERROR: {0}".format(name)

    def print_output(self, case_number, case_output):
        print "Case #{0}: {1}".format(case_number+1, case_output);

    def calculate_distance(self, pancakes):
        prevc = '+'
        count = 0
        points = []
        for c in range(len(pancakes)):
            if pancakes[c] != prevc:
                count += 1
                prevc = pancakes[c]
                points.append(c)
        return count, points

    def apply_flip(self, pancakes, index):
        if pancakes[index] == '+':
            pancakes[index] = '-'
        else:
            pancakes[index] = '+'
        return pancakes

    def apply_k_flip(self, pancakes, flip_start, flip_count):
        if len(pancakes) < flip_start + flip_count:
            print_error(sys._getframe(1).f_code.co_name)

        old_pancakes = pancakes[:]
        new_pancakes = pancakes[:]

        for i in range(flip_start, flip_start + flip_count):
            pancakes = self.apply_flip(new_pancakes, i)

        if self.debug: 
            print "{0} -> \n{1}".format(old_pancakes, new_pancakes)

        return new_pancakes

    def recursive_flip(self, pancakes, attempt, k):
        if attempt >= self.max_attempt:
            return self.max_attempt

        if self.debug:
            print "Attempt:{0} Pancakes:{1}".format(attempt, pancakes)

        distance, points = self.calculate_distance(pancakes)
        if distance == 0:
            if self.debug:
                print "**Attempt:{0} Pancakes:{1}".format(attempt, pancakes)
            self.max_attempt = attempt
            self.hist[''.join(pancakes)] = attempt
            return attempt

        if self.hist.has_key(''.join(pancakes)):
            return self.hist[''.join(pancakes)];
        
        self.hist[''.join(pancakes)] = self.max_attempt

        maxlen_pancakes = len(pancakes)

        for p in points:
            if p + k > maxlen_pancakes:
                break;

            new_pancakes = self.apply_k_flip(pancakes, p, k);
            new_dist, new_pts = self.calculate_distance(new_pancakes)

            #if new_dist <= distance:
            an_attempt = self.recursive_flip(new_pancakes, attempt+1, k)
            if an_attempt == attempt+1:
                return an_attempt

        return self.max_attempt

    def solve(self):
        for ncase in range(self.numcases):
            myperf = MyPerf(self.debug)
            myperf.timing_start(sys._getframe(1).f_code.co_name)
            line = self.inputf.readline()
            pancakes, k = line.split(' ')

            k = int(k)
            pancakes = list(pancakes)

            self.max_attempt = self.MAX_S
            self.hist = {}

            answer = self.recursive_flip(pancakes, 0, k)

            if answer >= self.MAX_S:
                answer = "IMPOSSIBLE"
            
            myperf.timing_end(sys._getframe(1).f_code.co_name)
            self.print_output(ncase, answer)


def print_usage():
    print "USAGE: %s <input file>".format(sys.argv[0])


if __name__ == "__main__":

    IFILE = None
    OFILE = None

    TIMING = False
    time_start = 0.0
    time_end = 0.0
    
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    for one_input_file in sys.argv[1:]:
        one = MySolution(one_input_file)
        one.solve()

