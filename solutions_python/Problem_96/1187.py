#
# Dancing with the Googlers
# Copyright 2012, Jesper Jurcenoks
# License: MIT
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Written in Python 2.7.2 for Windows



# Number pattern reseach shows that for every total score between 2 and 28 (inclusive, the is exactly 1 unsurprising score and 1 surprising score.
# For Total scores of 0,1,29,30 there is only trilet and it is unsurprising
# For Total scores where modulos 3 gives a 1, both the surprising and the unsurprising score has the same max point
# For Toal scores where modules 3 gives 0 or 2, the surprising score gives the higher max point.
# For any p all total scores >= (3*p-2) should be counted, and for p>1:  3*p-3 >= Scores >= 3*p-4 surprising triplets are used.

import re
import time
import multiprocessing

def count_func(inputdata):
    (testcase, N, S, p, ti) = inputdata
    count = 0
    cutoff = 3*p-2
    cutoff_surprising = 3*p-4
    for total in ti:
        if total >= cutoff:
            count +=1
        elif p>1 and total >= cutoff_surprising and S>0:
            count += 1
            S -= 1

    return (testcase, count)


if __name__ == '__main__':
    # load input file
    starttime = time.time()
    inputfile = file("input.txt")
    outputfile = file("output.txt", "w+")
    num_of_testcases = int(inputfile.readline())
    print num_of_testcases

    pool = multiprocessing.Pool()
    inputs = []

    for testcase in range(1,num_of_testcases+1):
        print "Load testcase: %s" % testcase
        in_str = inputfile.readline()
        result = re.split("\W+", in_str)
        N = int(result[0])
        S = int(result[1])
        p = int(result[2])
        ti = map(int, result[3:3+N])
        
        inputs.append((testcase, N,S, p, ti))
        print "%s: %s %s %s %s" % (testcase, N,S, p, ti)

    results = pool.map(count_func, inputs)

    for result in results:
        outstring = "Case #%s: %s\n" % result
        print outstring
        outputfile.write(outstring)
        
    outputfile.close()
    inputfile.close()

    endtime = time.time()
    print "time used %s:%s (%s)" % (int((endtime-starttime) / 60), int((endtime-starttime) % 60), endtime-starttime)
