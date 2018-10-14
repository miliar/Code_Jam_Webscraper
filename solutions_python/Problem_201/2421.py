import os, sys, time

#DEBUG = True
DEBUG = False 

class MyPerf:
    def __init__(self, onoff = True):
        if onoff == True:
            self.CHECK_PERF = True
        else:
            self.CHECK_PERF = False
        self.PERF = {}

    def timing_start(self, timing_key):
        if self.CHECK_PERF == True:
            self.PERF[timing_key] = time.clock()

    def timing_end(self, timing_key):
        if self.CHECK_PERF == False:
            return 0

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
    def __init__(self, inpf):
        self.inputf = open(inpf, 'r')
        self.numcases = int(self.inputf.readline())
        self.debug = DEBUG
        self.MAX_T = 100
        self.MAX_N = 10**18

    def print_error(self, name):
        print "ERROR: {0}".format(name)

    def print_output(self, case_number, a, b):
        print "Case #{0}: {1} {2}".format(case_number+1, a, b);

    def find_comfortable_stall(self):
        self.clean_stalls()
        start_index = -1;
        space_size = -1;

        for s in self.free_stalls:
            if self.free_stalls[s] == 0:
                continue
            if space_size < self.free_stalls[s]:
                space_size = self.free_stalls[s]
                start_index = s

        if self.debug:
            print "find_comfortable_stall: ind:{0} size:{1}".format(start_index, space_size)
        return start_index, space_size

    def clean_stalls(self):
        is_cleaned = True
        for s in self.free_stalls:
            if self.free_stalls[s] == 0:
                del self.free_stalls[s]
                is_cleaned = False
                break

        if is_cleaned == False:
            self.clean_stalls()

        return

    def allocate_stall(self):
        start_index, space_size = self.find_comfortable_stall()
        if space_size == -1: 
            return 0, 0

        mid_space = (space_size - 1) / 2
        mid_index = start_index + mid_space

        self.free_stalls[start_index] = mid_space
        self.free_stalls[mid_index+1] = space_size - mid_space - 1 

        self.occupied_stalls.append(mid_index)
        return self.free_stalls[start_index], self.free_stalls[mid_index+1]

    def allocate_stalls(self, total_stalls, total_people):
        self.free_stalls = {}
        self.free_stalls[0] = total_stalls
        self.occupied_stalls = []

        for i in range(total_people):
            ls, rs = self.allocate_stall()

            if self.debug:
                print "free stalls: {0}".format(self.free_stalls)
                print "occupied: {0}".format(self.occupied_stalls)

            if ls == 0 and rs == 0:
                break

        return ls, rs

    def solve(self):
        for ncase in range(self.numcases):
            myperf = MyPerf(self.debug)
            myperf.timing_start(sys._getframe(1).f_code.co_name)

            line = self.inputf.readline().strip()
            total_stalls, total_people = line.split(' ')

            ls, rs = self.allocate_stalls(int(total_stalls), int(total_people))

            myperf.timing_end(sys._getframe(1).f_code.co_name)
            self.print_output(ncase, max(ls, rs), min(ls, rs))


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

