#! /usr/bin/env python
import sys
import time

def get_series_by_index(r, index):
    return 2*(r+2*(index-1))+1

#req:  t > 2r+1
def solve(r, t):
    estimate = int(round( float(t) / float(2*r)))  #estimate is bigger than the answer.
    #excess = 2*r*estimate+ (2*estimate-1)*estimate  - t
    excess = estimate*(2*r + 2*estimate-1 ) - t
    print "estimate: "+str(estimate)+" excess:"+str(excess)
    while excess > 0:
        excess = excess - get_series_by_index(r, estimate)
        estimate = estimate - 1
    return estimate

if len(sys.argv) !=3:
    print "usage: input_file_path output_file_path"
    sys.exit(-1)

in_file = sys.argv[1]
out_file = sys.argv[2]
print "Reading from "+in_file+" and writing output to "+out_file

with open(in_file, 'r') as inFile:
    numTests = int(inFile.readline())

    with open(out_file, 'w') as outFile:
        for testNo in range(1, numTests+1):
            testArgs = inFile.readline().split(' ')
            
            answer = solve(int(testArgs[0]), int(testArgs[1]))
            out_str = "Case #"+str(testNo)+": "+str(answer)
            print out_str
            outFile.write(out_str+"\n")
