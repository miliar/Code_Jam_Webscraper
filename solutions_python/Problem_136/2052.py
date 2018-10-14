#!/usr/bin/env python

from sys import argv

class GCJInputReader:
    def __init__(self, file):
        self._file_handle = open(file)
        self._number_testcases = int(self._file_handle.readline())
    
    def __iter__(self):
        if hasattr(self, 'parse_testcase'):
            if callable(self.parse_testcase):
                self.next = self.parse_testcase
                return self
            else:
                raise NotImplementedError
        else:
            raise NotImplementedError
            
class CookieReader(GCJInputReader):
    def parse_testcase(self):
        input = self._file_handle.readline()
        if input == '':
            raise StopIteration()
        testcase = {}
        values = input.split(" ")
        testcase['C'] = float(values[0])
        testcase['F'] = float(values[1])
        testcase['X'] = float(values[2])
        return testcase
                
def solve_case(case):
    t = 0.0
    c = 0.0
    cps = 2.0
    cps_farm = testcase['F']
    c_win = testcase['X']
    c_farm = testcase['C']

    time_to_win = ( c_win - c ) / cps
    time_to_farm = ( c_farm - c ) / cps
    time_to_farm_break_even = c_farm / cps_farm

    while time_to_farm + time_to_farm_break_even < time_to_win:
        t += time_to_farm
        cps += cps_farm
        
        time_to_win = ( c_win ) / cps
        time_to_farm = ( c_farm  ) / cps
        time_to_farm_break_even = c_farm / cps_farm

    return str(t+time_to_win)
   
    
if __name__ == "__main__":
    c = CookieReader(argv[1])
    i = 1
    
    for testcase in c:
        print "Case #%i: %s " % (i, solve_case(testcase))
        i+=1
