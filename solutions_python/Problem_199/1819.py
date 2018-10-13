#!/usr/bin/env python
#coding:utf-8
#---------------------------------------------------------------------
import os
import sys
#---------------------------------------------------------------------
def getSolve(buf, K):
    buf = list(buf)
    K = int(K)
    cnt = 0
    while True:
        st = -1
        for i, b in enumerate(buf):
            if b == '-':
                st = i
                break
        if st == -1:
            return cnt
        elif len(buf) < st + K:
            return "IMPOSSIBLE"
        for i in range(st, st + K):
            if buf[i] == '-':
                buf[i] = '+'
            else:
                buf[i] = '-'
        cnt += 1
#        print buf
#---------------------------------------------------------------------
def main():
    if len(sys.argv) == 2:
        if os.path.isfile(sys.argv[1]) is False:
            print "dose not found file", sys.argv[1]
            return
        i = 0
        with open(sys.argv[1], 'r') as f:
            buffs = f.readlines()
            for i, buff in enumerate(buffs):
                if i != 0:
                    buff = buff.strip()
                    b = buff.split(' ')
#                    print buff
                    print 'Case #%d: %s'% (i ,getSolve(b[0], b[1]))
                i += 1
#---------------------------------------------------------------------
if __name__ == '__main__':
    main()
#---------------------------------------------------------------------
