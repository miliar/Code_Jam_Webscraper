
# -*- coding: cp932 -*-

import sys

def debug(msg):
    #return
    sys.stderr.write(msg)
    sys.stderr.flush()
    

def main(A,B,K):
    ans = 0
    for i in range(A):
        for j in range(B):
            if (i & j < K):
                ans += 1
    return str(ans)

inputfile = "B-small-attempt0.in"
f = open(inputfile)
sys.stdout = open(inputfile.replace(".in", ".txt"),'w')
tc_num = int(f.readline().rstrip())

for tc in range(tc_num):
    l = f.readline().split()
    A = int(l[0])
    B = int(l[1])
    K = int(l[2])
    ans = main(A,B,K)
    print("Case #" + str(tc+1) + ": " + ans)

   
