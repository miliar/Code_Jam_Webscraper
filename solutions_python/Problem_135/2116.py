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
            
class MagicianReader(GCJInputReader):
    def parse_testcase(self):
        testcase = {}
        # 1st line is fist answer
        try:
            testcase['firstanswer'] = int(self._file_handle.readline())
        except ValueError:
            raise StopIteration()
        # 2nd-5th line is first card layout
        testcase['firstlayout'] = []
        for i in range(4):
            input = self._file_handle.readline()
            testcase['firstlayout'].append([int(j) for j in input.split(" ")])
        # 6th line is second answer
        testcase['secondanswer'] = int(self._file_handle.readline())
        testcase['secondlayout'] = []
        for i in range(4):
            input = self._file_handle.readline()
            testcase['secondlayout'].append([int(j) for j in input.split(" ")])

        return testcase
        
def solve_case(case):
    first_line = case['firstlayout'][case['firstanswer']-1]
    second_line = case['secondlayout'][case['secondanswer']-1]
    
    same_cards = []
    for card_one in first_line:
        for card_two in second_line:
            if card_one == card_two:
                same_cards.append(card_one)

    if len(same_cards) > 1:
        return "Bad Magician!"
    elif len(same_cards) == 1:
        return str(same_cards[0])
    else:
        return "Volunteer cheated!" 

if __name__ == "__main__":
    m = MagicianReader(argv[1])
    i = 1
    
    for testcase in m:
        print "Case #%i: %s " % (i, solve_case(testcase))
        i+=1
