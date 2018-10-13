import sys ;

"""
class TestcaseReader :
    def __init__(self, IFD) :
        self.ifd = IFD
        return self
class TestcaseInput :
    def __init__(
class TestcaseOutput :
class TestcaseWriter :
    

class ProblemSolver : 
    def __init__(self):
        return self ; 
    def Main(argv) :
        inputFileName = argv[1]
        outputFileName = argv[2]
        inputFileDescriptor = fopen(inputFileName, "r")
        outputFileDescriptor = fopen(outputFileName, "w") 
        noOfTestCases = int(inputFileDescriptor.read())

        for i in range(noOfTestCases) :
            testcaseDetail = self.testcasReader(inputFileDescriptor)
            testcaseoutput = self.Solver(testcaseDetail)
            self.testcaseWriter(testcaseOutput, outputFileDescriptor)
        inputFileDescriptor.close()
        outputFileDescriptor.close() 
        return
if __name__ == "__main__" :
    p = ProblemSolver()
    p.Main(sys.argv) 
"""
import sys
import os

ifd = open("small.in", "r")
ofd = open("out.txt", "w")  
no_of_testcase = int(ifd.readline())
item_map = {} 
for i in range(no_of_testcase) :
    choice_array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    first_choice_value = int(ifd.readline()) 
    for row in range(4) : 
        row_value = ifd.readline() ; 
        if row == first_choice_value - 1 : 
            row_content_arr = row_value.split()
            for row_elm in row_content_arr :
                choice_array[int(row_elm) - 1] = 1 ;
    second_choice_value = int(ifd.readline())
    test_status = 0
    test_index = 0  
    for row in range(4) :
        row_value = ifd.readline() ;
        if row == second_choice_value - 1 :
            row_content_arr = row_value.split() ;
            for row_elm in row_content_arr : 
                if(choice_array[int(row_elm) - 1] == 1) : 
                    if test_index == 0 :
                        test_index = int(row_elm) 
                    else :
                        test_status = 1 
    if test_status == 0 : 
        if test_index == 0 : 
            ofd.write("Case #"+ str(i+1) + ": Volunteer cheated!\n")
        else :
            ofd.write("Case #"+ str(i+1) + ": " + str(test_index) + "\n") 
    else :
        ofd.write("Case #"+ str(i+1) + ": Bad magician!\n") 
ifd.close()
ofd.close()


