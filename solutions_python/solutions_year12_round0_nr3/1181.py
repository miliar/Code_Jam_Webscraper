# Recycled Numbers
# Copyright 2012, Jesper Jurcenoks
# License: MIT
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Written in Python 2.7.2 for Windows

import re


def count_recycled(A,B):
    recycled = 0
    pair_set = set()
    #run through all numbers between A and B
    for n in range(A, B):
        n_str = str(n)
        for shift in range(1,len(n_str)):
            m = int(n_str[shift:]+n_str[:shift])
            m_str = str(m)
            if (len(n_str) == len(m_str)) and (n < m) and (m <= B):
                if (n_str, m_str) not in pair_set:
                    pair_set.add((n_str, m_str))
#                    print "reclyced pair (%s, %s)" % (n,m)
                    recycled += 1
    return recycled

# load input file
inputfile = file("input.txt")
outputfile = file("output.txt", "w+")
num_of_testcases = int(inputfile.readline())
print num_of_testcases
for testcase in range(1,num_of_testcases+1):
    print "Load testcase: %s" % testcase
    int_pair_str = inputfile.readline()
    result = re.search("([0-9]+) ([0-9]+)", int_pair_str)
    A = int(result.group(1))
    B = int(result.group(2))

    print A,B
    
    outstring = "Case #%s: %s\n" % (testcase, count_recycled(A,B))
    print outstring
    outputfile.write(outstring)
outputfile.close()
inputfile.close()
