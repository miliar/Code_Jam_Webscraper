#!/usr/bin/env python3
#coding:utf-8
#---------------------------------------------------------------------
import os
import sys
#---------------------------------------------------------------------
def isTidy(num):
    buf = str(num)
    if len(buf) == 1:
        return True
    for i in range(1, len(buf)):
        if buf[i-1] > buf[i]:
            return False
    return True
#---------------------------------------------------------------------
def getSolve(num):
    buf = list(num)
    num = int(num)
    nn = 0
    xx = 0
    yy = 0
    for i, b in enumerate(buf):
        if nn < int(b):
            xx = i
            nn = int(b)
        elif nn == int(b):
            nn = int(b)
        elif nn > int(b):
            yy = i
            break
#    print(num, xx, yy)
    if yy == 0:
        return num
    for i in range(xx+1, len(buf)):
        buf[i] = '0'
    num = int(''.join(buf))
    #print(num)
    for i in range(num,1, -1):
#        print("->%d" % i)
        if isTidy(i) is True:
            return i
#---------------------------------------------------------------------
def main():
    if len(sys.argv) == 2:
        if os.path.isfile(sys.argv[1]) is False:
            print("dose not found file:%s" % sys.argv[1])
            return
        i = 0
        with open(sys.argv[1], 'r') as f:
            buffs = f.readlines()
            for i, buff in enumerate(buffs):
                if i != 0:
                    buff = buff.strip()
#                    print buff
                    print('Case #%d: %s' % (i ,getSolve(buff)))
                i += 1
#---------------------------------------------------------------------
if __name__ == '__main__':
    main()
#---------------------------------------------------------------------
