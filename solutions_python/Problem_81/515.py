#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def solve(sche):
    N = len(sche)
    
    wp = []
    for row in sche:
        r = [x for x in row if x != -1]
        wp.append(sum(r) / len(r))
    print("wp =", wp)

    owp = []
    for i, row in enumerate(sche):
        owp0 = 0
        s = 0
        cnt = 0
        for j, col in enumerate(row):
            if i != j and col != -1:
                # team j の team i 以外との対戦の勝率を計算
                wpj = 0
                wpjc = 0
                for k, c in enumerate(sche[j]):
                    if k == i:
                        continue
                    if c == 1:
                        wpj += 1
                    if c != -1:
                        wpjc += 1
                print("i, j, owpj =", i, j, wpj / wpjc)
                s += wpj / wpjc
                cnt += 1
        owp.append(s / cnt)
    print("owp =", owp)
    
    oowp = []
    for row in sche:
        print(row)
        s = 0
        cnt = 0
        for j, col in enumerate(row):
            if col != -1:
                print(j, owp[j])
                s += owp[j]
                cnt += 1
        oowp.append(s / cnt)
        print(s/cnt)
    print("oowp =", oowp)
    
    rpi = []
    for i in range(N):
        rpi.append(0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i])
    
    return rpi
    
                

#
# main
#
if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    file = "sample.in"

with open(file, "r") as f:
    with open(file + ".output", "w") as output:
        T = int(f.readline())

        for n in range(1, T+1):
            sche = []
            N = int(f.readline())
            for i in range(N):
                sche.append([])
                for ch in f.readline().rstrip():
                    if ch == ".":
                        sche[i].append(-1)
                    else:
                        sche[i].append(int(ch))
                
            print(sche)
            result = solve(sche)
    
            msg = "Case #%d:" % n
            print(msg)
            output.write(msg + "\n")
            for rpi in result:
                msg = "%f" % rpi
                print(msg)
                output.write(msg + "\n")
