import string
import math

testcase = open('testcase', 'r')
num_cases = int(string.strip(testcase.readline()))

for i in xrange(1, num_cases+1):
    params = string.split(string.strip(testcase.readline()), ' ')
    a = int(params[0])
    b = int(params[1])
    k = int(params[2])
    winners = 0
    for n in xrange(a):
        for m in xrange(b):
            if n&m < k:
               winners += 1
    print "Case #"+str(i)+": "+str(winners)
