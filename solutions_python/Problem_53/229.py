# -*- coding: utf-8 -*-
import sys
fin = sys.stdin
N = int(fin.readline())
for case in range(1,N+1):
    code = map(int, fin.readline().split())
    if(code[1] % (1<<code[0]) == ((1<<(code[0])) -1)):
        print "Case #%d: ON" % (case)
    else:
		print "Case #%d: OFF" % (case)
    
