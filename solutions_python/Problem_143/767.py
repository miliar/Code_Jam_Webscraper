'''
Created on May 3, 2014

@author: Miguel Provencio
'''
from sys import stdin,argv,stdout,stderr

def iterate(A,B,K):
    count = 0
    for i in xrange(A):
        for j in xrange(B):
            num = i & j
            if num < K:
                count += 1
    return count


infile = stdin
outfile = stdout

cases = int(infile.readline())
for i in xrange(cases):
    case = i + 1
    line = infile.readline()
    args = line.split(" ")
    A = int(args[0])
    B = int(args[1])
    K = int(args[2])
    count = iterate(A,B,K)
    outfile.write("Case #%d: %d\n" % (case,count))    
