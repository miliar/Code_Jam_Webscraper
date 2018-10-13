
# -*- coding: cp932 -*-

import sys
import math

def debug(msg):
    #return
    sys.stderr.write(msg)
    sys.stderr.flush()
    


def solve(f,C):
    used = [False for i in range(len(f))]
    ans = 0
    for i in range(len(f)):
        if used[i]:
            tmp = 0
            for j in range(i+1,len(f)):
                if not used[j]: tmp += 1
            return str(ans + math.ceil(tmp/2))

        for j in range(i+1,len(f)):
            if used[j]: continue
            if f[i] + f[j] <= C:
                used[j] = True
                break
        used[i] = True
        ans += 1

            
    return str(ans)
    

inputfile = "A-large.in"
f = open(inputfile)
sys.stdout = open(inputfile.replace(".in", ".txt"),'w')
tc_num = int(f.readline().rstrip())

for tc in range(tc_num):
    l = f.readline().split() 
    N = int(l[0])
    C = int(l[1])
    F = []
    l = f.readline().split()
    for i in range(N):
#        for j in range(1000):
        F.append(int(l[i]))

    F.sort(reverse=True)
    
    ans = solve(F,C)
    debug("Case " + str(tc+1) + "\n")
    print("Case #" + str(tc+1) + ": " + ans)

   
