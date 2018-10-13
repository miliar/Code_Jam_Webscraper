#!/usr/bin/python
import sys, time

limit = 1000000

def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                #nb str[0:1] works in both string and list contexts
                yield perm[:i] + str[0:1] + perm[i:]



def run(case, curr=None):
    ans = ''
    time1 = time.time()    
    
    if curr == None:
        curr = case
    List = []
    for x in all_perms(case):
        List.append(int(x))
        
    #remove dups and sort
    List = list(set(List))
    List.sort()
    
    #print case, curr, len(List), List
    currI = List.index(int(curr))
    #print currI
    if currI != len(List) - 1:
        next = currI + 1
        return List[next]
    else:
        return run(case + '0', case)
        
    
if len(sys.argv) < 2:
  print "file needed"
  exit()
infile = sys.argv[1]
try:
  f = open(infile, 'r')
except IOError:
  print "File open error"
  exit()



#read num cases
numCases= f.readline()

#gen cases
cases = []
for i in range(int(numCases)):
   cases.append(f.readline().strip())

time0 = time.time()

outfile = open('output.out', 'w')
for i in range(len(cases)):
    case = cases[i]
    ans = run(case)    
    print ans
    outfile.write('Case #' + str(i+1) +': ' + str(ans) + '\n')
    
outfile.close()   
print time.time()-time0
    
