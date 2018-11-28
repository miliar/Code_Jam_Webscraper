'''
Created on 2012/04/14

@author: hanaue51
'''
import os
os.chdir("../../../data/2012/qualification/")
filename = "C-small-attempt0"
postfix_in = ".in"
postfix_out = ".out"
format = "Case #%d: %d\n"

infile = open(os.getcwd() + "/" + filename + postfix_in, "r")
lines = infile.readlines()
infile.close()

n_cases = int(lines[0].strip())
results = []
for i in xrange(1, len(lines)):
    elems = lines[i].strip().split()
    min = int(elems[0])
    max = int(elems[1])
    answer = 0
    for n in xrange(min, max + 1):
        n_str = str(n)
        for l in xrange(1, len(n_str)):
            n_str = n_str[1:] + n_str[0]
            m = int(n_str)
            if min <= m and m <= max and n < m:
                answer += 1
    results.append(format % (i, answer))

#print results
outfile = open(os.getcwd() + "/" + filename + postfix_out, "w")
for result in results:
    outfile.write(result)
outfile.close()
