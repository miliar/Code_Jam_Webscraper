# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys

with open(sys.argv[1], "r") as f:
    count = int(f.readline())
    
    out = []
    for i in range(count):
        S, N = f.readline().split(" ")
        S = list(S)
        N = int(N)
        #print(S)
        #print(N)
        
        flip_count = 0
        for ii in range(len(S) - N + 1):
            if S[ii] == "-":
                flip_count += 1
                for iii in range(N):
                    if S[ii + iii] == "-":
                        S[ii + iii] = "+"
                    else:
                        S[ii + iii] = "-"
        if "-" not in S:
            out.append("Case #%d: %d\n"%(i+1, flip_count))
        else:
            out.append("Case #%d: IMPOSSIBLE\n"%(i+1))
        print(S)

with open(sys.argv[1] + "_out.txt", "w") as f:
    f.writelines(out)
        
