# Speaking in tongues, google Code Jam 2012
# Copyright 2012, Jesper Jurcenoks
# License: MIT
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Written in Python 2.7.2 for Windows

import re
import string

# load input file
inputfile = file("input.txt", "r")
outputfile = file("output.txt", "w+")
num_of_testcases = int(inputfile.readline())
intable = "qzejp mysljylc kd kxveddknmc re jsicpdrysi"+"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"+"de kr kd eoya kw aej tysr re ujdr lkgc jv"
outtable = "zqour language is impossible to understand"+"there are twenty six factorial possibilities"+"so it is okay if you want to just give up"
translationtable = string.maketrans(intable, outtable)


print num_of_testcases
for testcase in range(1,num_of_testcases+1):
    print "Load testcase: %s" % testcase
    googlerese = inputfile.readline().strip()
    print googlerese

    translated = googlerese.translate(translationtable)
    outstring = "Case #%s: %s\n" % (testcase, translated)
    print outstring
    outputfile.write(outstring)
outputfile.close()
inputfile.close()
