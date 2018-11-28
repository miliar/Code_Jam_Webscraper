import sys
import re #regular expressions, string pattern matching
import math #math stuff
import array #more efficient lists (type constraint)

def solve(input, numcount):
  found = False
  while found == False:
    owncount = [0,0,0,0,0,0,0,0,0,0]
    count = input
    last = 0
    while count > 9:
       last = count % 10
       if not (last == 0):
            if owncount[last] == numcount[last]:
                #more numbers already
                owncount[last] += 1
                break
            else:
                owncount[last] += 1
       count = count / 10
       #print count
    if not (count == 0) and count < 10:
        owncount[count] += 1
    if owncount == numcount:
        found = True
    else:
        input +=1
  return input

if __name__ == "__main__":
    cases = int(sys.stdin.readline().strip())
    for case in range(1,cases+1):
        print "Case #{0}:".format(case),
        #read and format input here
        input = int(sys.stdin.readline().strip())
        numcount = [0,0,0,0,0,0,0,0,0,0]
        count = input
        last = 0
        while count > 9:
            last = count % 10
            if not (last == 0):
                numcount[last] += 1
            count = count / 10
        #print count
        if not (count == 0):
            numcount[count] += 1
        #print numcount
        #print solution
        print solve(input+1, numcount);