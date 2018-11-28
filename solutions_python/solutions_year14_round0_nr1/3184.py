#!/usr/env python
#
import re
import sys

class Solver:
    def __init__(self,start,lines):
        self.start=start
        self.lines = lines
        self.next_start = start + 10
        
    def isCheat(self):
        for element in self.row1:
            if element in self.row2:
                return False
        return True
    
    def badMagic(self):
        have_match = False
        #print self.row2
        for element in self.row1:
            if element in self.row2:
                if have_match:
                    return True
                else:
                    have_match = True
        return False
    
    def findCard(self):
        for element in self.row1:
            if element in self.row2:
                return element

                
        
    def solveCase(self):
        #first group
        row_num = int(self.lines[self.start])
        row_index = self.start + int(row_num)
        self.row1 = re.split(' ',self.lines[row_index].strip())
        
        #Second group
        second_start = self.start + 5
        row_num = int(self.lines[second_start])
        row_index = second_start + row_num       
        self.row2 = re.split(' ',self.lines[row_index].strip())
        

        if self.badMagic():
            return "Bad magician!"
        elif self.isCheat():
            return "Volunteer cheated!"
        else:
            return str(self.findCard())
        
             
    
        
def runCases(input_file):
    lines = open(input_file).readlines()
    
    number_of_cases = int(lines[0])
    cases = []
    start_point = 1
    for case_num in range(1,number_of_cases+1):
        s = Solver(start_point,lines)
        result = s.solveCase()
        print "Case #" + str(case_num) + ": " + str(result)
        start_point = s.next_start
        
if __name__ == "__main__":
    runCases(sys.argv[1])


        
    