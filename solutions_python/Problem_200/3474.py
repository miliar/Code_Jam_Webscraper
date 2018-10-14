import os, sys, time

DEBUG = False 

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
    def __init__(self, inpf):
        self.inputf = open(inpf, 'r')
        self.numcases = int(self.inputf.readline())
        self.debug = DEBUG
        self.MAX_T = 100
        self.MAX_N = 10**18
        self.numarr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.numarrlen = len(self.numarr)

    def print_error(self, name):
        print "ERROR: {0}".format(name)

    def print_output(self, case_number, case_output):
        print "Case #{0}: {1}".format(case_number+1, case_output);

    def check_tidynumber(self, tidynumber):
        check_result = True
        check_index = -1
        len_tidynumber = len(tidynumber)

        if len_tidynumber == 1:
            return check_result, check_index

        for i in range(len_tidynumber - 1):
            if (tidynumber[i] > tidynumber[i+1]):
                check_result = False
                check_index = i
                break;

        return check_result, check_index


    def make_tidy(self, num):
        check_result, check_index = self.check_tidynumber(num)
        if check_result == True:
            return num

        untidynum = list(num)

        if self.debug:
            print "make_tidy: untidynum: {0}".format(''.join(untidynum))

        is_carry = False
        check_num = int(untidynum[check_index])

        if check_num > 0:
            if self.debug:
                print "make_tidy: subtracting from {0}".format(check_num)
            untidynum[check_index] = self.numarr[check_num - 1] 
        else:
            is_carry = True
            untidynum[check_index] = self.numarr[9]

        if check_index + 1 < len(untidynum):
            for i in range(check_index+1, len(untidynum)):
                untidynum[i] = self.numarr[9]
      
        if is_carry:
            if self.debug:
                print "make_tidy: upperpart: {0}".format(''.join(untidynum[0:check_index]))
            upper_part = int(''.join(untidynum[0:check_index]))
            upper_part -= 1
            upper_part_list = list(str(upper_part))
            upper_part_list.append(untidynum[check_index:end])
            untidynum = upper_part_list

        if check_num == 1 and check_index == 0:
            del untidynum[0]

        return self.make_tidy(untidynum)

    def solve(self):
        for ncase in range(self.numcases):
            myperf = MyPerf(self.debug)
            myperf.timing_start(sys._getframe(1).f_code.co_name)

            line = self.inputf.readline().strip()
            untidynum = list(line)

            check_result, check_index = self.check_tidynumber(untidynum)

            if check_result == False:
                tidynum = self.make_tidy(untidynum)
            else:
                tidynum = untidynum

            myperf.timing_end(sys._getframe(1).f_code.co_name)
            self.print_output(ncase, ''.join(tidynum))


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

