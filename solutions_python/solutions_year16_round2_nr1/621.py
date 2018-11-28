import sys
from collections import deque as dq

rd = open("A-large.in","r")
wrt = open("A.out", "w")

def fun(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 0
        d[i] += 1
    return d

def bld():
    d = {"ZERO":0, "ONE":1, "TWO":2, "THREE":3, "FOUR":4, "FIVE":5, "SIX":6, "SEVEN":7, "EIGHT":8, "NINE":9}
    return d

def solve(d):
    nm = []
    if "Z" in d:
        tmp = d["Z"]
        for i in xrange(tmp):
            nm.append(0)
            d["E"] -= 1
            d["R"] -= 1
            d["O"] -= 1
        d["Z"] = 0
    if "W" in d:
        tmp = d["W"]
        for i in xrange(tmp):
            nm.append(2)
            d["T"] -= 1
            d["O"] -= 1
        d["W"] = 0
    if "U" in d:
        tmp = d["U"]
        for i in xrange(tmp):
            nm.append(4)
            d["F"] -= 1
            d["O"] -= 1
            d["U"] -= 1
            d["R"] -= 1
    if "F" in d:
        tmp = d["F"]
        for i in xrange(tmp):
            nm.append(5)
            d["F"] -= 1
            d["I"] -= 1
            d["V"] -= 1
            d["E"] -= 1
    if "X" in d:
        tmp = d["X"]
        for i in xrange(tmp):
            nm.append(6)
            d["S"] -= 1
            d["I"] -= 1
            d["X"] -= 1
    if "G" in d:
        tmp = d["G"]
        for i in xrange(tmp):
            nm.append(8)
            d["E"] -= 1
            d["I"] -= 1
            d["G"] -= 1
            d["H"] -= 1
            d["T"] -= 1
    if "V" in d:
        tmp = d["V"]
        for i in xrange(tmp):
            nm.append(7)
            d["S"] -= 1
            d["E"] -= 2
            d["V"] -= 1
            d["N"] -= 1
    if "T" in d:
        tmp = d["T"]
        for i in xrange(tmp):
            nm.append(3)
            d["T"] -= 1
            d["H"] -= 1
            d["R"] -= 1
            d["E"] -= 2
    if "O" in d:
        tmp = d["O"]
        for i in xrange(tmp):
            nm.append(1)
            d["O"] -= 1
            d["N"] -= 1
            d["E"] -= 1
    if "I" in d:
        tmp = d["I"]
        for i in xrange(tmp):
            nm.append(9)
            d["N"] -= 2
            d["I"] -= 1
            d["E"] -= 1
    nm.sort()
    nm = "".join(str(i) for i in nm)
    return nm

for test in xrange(1, int(rd.readline().strip()) + 1):
    s = (rd.readline().strip())
    d = fun(s)
    nm = solve(d)
    ans = "Case #%d: %s\n" %(test, nm)
    wrt.write(ans)
    
wrt.close()
