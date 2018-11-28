#!/usr/bin/env python

def nwd(a, b):
    if b == 0:
        return a
    return nwd(b, a%b)

if __name__ == "__main__":
    lw = int(raw_input())
    for l in range(lw):
        case = raw_input()
        dane = case.split()
        n = int(dane[0])
        dane = dane[1:]
        dane = [long(i) for i in dane]
        dane.sort()
        T = dane[1] - dane[0]
        for i in range(n-1):
           roz = dane[i+1] - dane[i]
           T = nwd(T, roz)
        y = (T - (dane[0]%T))%T
        print "Case #" + str(l+1) + ":", y
