#!/usr/bin/python3
__author__ = 'Tianren Liu'

import sys
import numpy as np

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _t in range(1,T+1):
        N, R, O, Y, G, B, V = map(int, sys.stdin.readline().split())
        # print("R{}, O{}, Y{}, G{}, B{}, V{}".format(R, O, Y, G, B, V))

        r,y,b = R-G, Y-V, B-O
        res = ""
        if 2*max(r,y,b) > r+y+b:
            res = "IMPOSSIBLE"
        elif R==G > 0:
            if max(Y,V,B,O) != 0:
                res = "IMPOSSIBLE"
            else:
                res = "RG"*R
        elif Y==V > 0:
            if max(R,G,B,O) != 0:
                res = "IMPOSSIBLE"
            else:
                res = "YV"*Y
        elif B==O > 0:
            if max(R,G,Y,V) != 0:
                res = "IMPOSSIBLE"
            else:
                res = "BO"*B
        else:
            N = [n for n,c in sorted([(r,'R'),(y,'Y'),(b,'B')], reverse=True)]
            C = [c for n,c in sorted([(r,'R'),(y,'Y'),(b,'B')], reverse=True)]
            while max(N) != 0:
                # print (res,N,C)
                nxt = 0
                if len(res) == 0:
                    nxt = 0
                elif N[2] > N[0] + N[1]:
                    nxt = 2
                elif res[-1] != C[0] and N[0] > 0:
                    nxt = 0
                else:
                    nxt = 1
                res += C[nxt]
                N[nxt] -= 1
                if G>0 and C[nxt] == 'R':
                    res+='GR'*G
                    G = 0
                if V>0 and C[nxt] == 'Y':
                    res+='VY'*G
                    V = 0
                if O>0 and C[nxt] == 'B':
                    res+='OB'*G
                    O = 0
        print("Case #{}: {}".format(_t, res))
