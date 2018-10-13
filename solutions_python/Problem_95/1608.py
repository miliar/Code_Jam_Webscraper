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
import string
class SITTranslator:
    def __init__(self):
        input_str = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
y qee
z"""
        output_str = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
a zoo
q"""
        i = str(filter(lambda x: x!=" " and x!="\n", list(input_str)))
        o = str(filter(lambda x: x!=" " and x!="\n", list(output_str)))
        self.translate_table = string.maketrans(i, o)

    def translate(self, in_str):
        return string.translate(in_str, self.translate_table)

if __name__ == "__main__":         
    i = GCJIn()
    o = GCJOut()
    t = SITTranslator()
    for num, line in enumerate(i.lines):
        o.write(num+1, t.translate(line))
     
