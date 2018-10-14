# -*- coding: utf-8 -*-
import sys
import math

stin = sys.stdin
stin.readline() # 1行読み飛ばし


for no,line in enumerate(stin.readlines()):
    cnt = 0
    (n,m) = map(int, line.split())
    for i in range(n, m+1):
        tbl = {}
        num = i
        stri = str(i)
        #if "0" in stri: continue
        keta = len(stri)
        for k in range(keta-1):
            num = (num / 10) + (num % 10) * (10 ** (keta-1))
            if i < num and num <= m:
                tbl[(i,num)] = 1
        cnt += len(tbl)

    print("Case #%d: %d" % (no+1, cnt))
            
        
    
