#!/usr/bin/env python
#Template Version v1
import numpy as np
import pandas as pd
import math
from collections import defaultdict as dd

def main():
    file_size = 's2'
    inf = open(file_size + ".in","r")
    outf = open(file_size + ".out","w")
    cases = int(inf.readline())
    cn = 0
    for line in inf:
        cn += 1
        n, k = map(lambda x: int(x), line.split(' '))
        #main logic here:
        row = int(math.log(k,2))
        seat = k - 2**row
        print row, seat
        sec = dd(lambda:0, {n:1})

        for i in range(row):
            newsec = dd(lambda:0, {})
            for k in sec:
                if k & 1 :
                    newsec[(k-1)/2] = newsec[(k-1)/2] + 2*sec[k]
                else :
                    newsec[k/2] = newsec[k/2] + sec[k]
                    newsec[k/2 - 1] = newsec[k/2 - 1] + sec[k]
            sec = newsec
        
        if sec[max(sec.keys())] >= seat+1:
            ns = max(sec.keys())
        else:
            ns = max(sec.keys()) - 1
        
        print ns
        a = (ns-1)/2
        b = a
        if ns & 1 == 0:
            a += 1

        answer = "Case #{}: {} {}\n".format(cn,a,b)
        print(answer)
        outf.write(answer)
        
    inf.close()
    outf.close()

if __name__ == "__main__":
    main()

