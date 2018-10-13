#!/usr/bin/python

#Generic code for this competition
import sys
import time
class GCJIn:
    def __init__(self):
        try:
            f = open(sys.argv[1])
            #Read in lines and strip \n if it is in the file
            self.lines = map(lambda x: 
                             filter(lambda y: y!="\n",x),
                             f.readlines())
            self.casecount = self.lines[0]
            self.lines.pop(0)
            f.close()

        except IndexError:
            print "No file argument provided!"
            exit()
   
class GCJOut:
    def __init__(self):
        fname = str(time.time()).split(".")[0]+"output.out"
        self.f = open(fname, 'w') 
 
    def __del__(self):
        try:
            self.f.close()
        except:
            print "Error closing output file! Make sure EOF was written"

    def write(self, case_num, out):
        s = "Case #" + str(case_num)+ ": " + str(out) + "\n"
        self.f.write(s)

    def _print(self, case_num, out):
        print "Case #" + str(case_num)+ ": " + str(out)

#Challenge specific code

if __name__=="__main__":
    i = GCJIn()
    o = GCJOut()
    for num, line in enumerate(i.lines):
        formatted = map(int, line.split(" "))
        num_googlers = formatted[0]
        surprise_max = formatted[1]
        bar = formatted[2]
        scores = formatted[3:]
        
        #Lowest possible scores for surprise and regular conditions
        low_surprise = (bar-2) if bar-2 >= 0 else 0
        low_regular = (bar-1) if bar-1 >= 0 else 0
        min_surprise = sum([bar, low_surprise, low_surprise])
        min_regular = sum([bar, low_regular, low_regular])

        #Find possible surprise values
        reduced = filter(lambda x: x >= min_surprise, scores)
        reduced = filter(lambda x: x < min_regular, reduced)
 
        #Find regular values 
        regular = filter(lambda x: x >= min_regular, scores)
       
        o.write(num+1, len(regular) + min(len(reduced), surprise_max))

