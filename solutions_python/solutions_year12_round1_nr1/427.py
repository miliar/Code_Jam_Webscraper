#
# Password
# Copyright 2012, Jesper Jurcenoks
# License: MIT
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Written in Python 2.7.2 for Windows



import re
import time
import multiprocessing

def func(inputdata):
    (testcase, A, B, Ps) = inputdata

    #press enter right away
    expected = B + 2
    min_keystrokes = expected

    #delete N chars
    for n in range(A, -1, -1):
        keystrokes = n + (B - n) + 1
        # Calculate probability that A-n chars are right
        if Ps[0:A-n] == []:
            right_probability = 1
        else:
            right_probability = reduce(lambda x,y: x*y, Ps[0:A-n])
        wrong_probability = 1 - right_probability
        keystrokes_by_right = B + n + 1 -(A-n)
        keystrokes_by_wrong = keystrokes_by_right + B + 1
        average_keystrokes = (right_probability * keystrokes_by_right) + (wrong_probability * keystrokes_by_wrong)
        print "testcase: %s, Deleted %s, Wrong_Prob: %s, right_prob: %s, Wrong_Keystrokes:%s, right_keystrokes: %s, average_keystrokes: %s" %(testcase, n, wrong_probability, right_probability, keystrokes_by_wrong, keystrokes_by_right, average_keystrokes)
            
        min_keystrokes = min(min_keystrokes, average_keystrokes)


    return (testcase, min_keystrokes)


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
        print result
        A = int(result[0]) #already typed
        B = int(result[1]) # total numbers in password

        in_str = inputfile.readline()
        result = re.split(" ", in_str)
        print result
        Ps = map(float, result)
        inputs.append((testcase, A, B, Ps))
        
        print "%s: %s %s %s" % (testcase, A, B, Ps)

    results = pool.map(func, inputs)

    for result in results:
        outstring = "Case #%s: %s\n" % result
        print outstring
        outputfile.write(outstring)
        
    outputfile.close()
    inputfile.close()

    endtime = time.time()
    print "time used %s:%s (%s)" % (int((endtime-starttime) / 60), int((endtime-starttime) % 60), endtime-starttime)
