
# -*- coding: cp932 -*-

import sys

def debug(msg):
    #return
    sys.stderr.write(msg)
    sys.stderr.flush()
    
def solve(n):
    ans = 0
    while(len(n) > 1):
        minInd = n.index(min(n))
    
        ans += min(minInd,len(n)-1 -minInd)
        n.pop(minInd)
        
    return ans

def main(n):
    return str(solve(n))

inputfile = "B-large.in"
f = open(inputfile)
sys.stdout = open(inputfile.replace(".in", ".txt"),'w')
tc_num = int(f.readline().rstrip())

for tc in range(tc_num):
    N = int(f.readline().rstrip())
    n = []
    l = f.readline().split()
    for i in range(N):
        n.append(int(l[i]))
        
    ans = main(n)
    print("Case #" + str(tc+1) + ": " + ans)

   
