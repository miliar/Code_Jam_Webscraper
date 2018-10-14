#!/usr/bin/python
# -*- coding:utf-8 -*-
import os

def judge():
    try:
        fin = open("A-small-attempt0.in", "r")
        fout = open("a.out", "w")
        t = int(fin.readline())
        for i in range(t):
            x = int(fin.readline())
            d1 = []
            for j in range(4):
                if j != x-1:
                    fin.readline()
                    continue
                d1 = fin.readline().strip().split()
            x = int(fin.readline())
            d2 = []
            for j in range(4):
                if j != x-1:
                    fin.readline()
                    continue
                d2 = fin.readline().strip().split()
            d = set(d1) & set(d2)
            tmp = len(d)
            if tmp == 0:
                fout.write("Case #%d: Volunteer cheated!\n"%(i+1))
            elif tmp == 1:
                fout.write("Case #%d: %s\n"%(i+1, list(d)[0]))
            else:
                fout.write("Case #%d: Bad magician!\n"%(i+1))
        fin.close()
        fout.close()
    except Exception,e:
        #print e
        pass


if __name__ == "__main__":
    judge()


