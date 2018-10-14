#!/usr/bin/python

from __future__ import print_function
import sys
from itertools import islice

def Tf(v0, C, F, X):
    s = 0.0
    N = 0
    while True:
        yield N, (s + float(X) / (v0 + N*F))
        s += C / (v0 + N*F)
        N += 1

def plot(t, N):
    from subprocess import Popen, PIPE
    plot = Popen("tplot -e 'plot STDIN using N:T w l' -p", shell=True, stdin=PIPE)
    print("# N T", file=plot.stdin)
    for Ni, Ti in islice(t, N):
        print(Ni, "\t", Ti, file=plot.stdin)
    plot.stdin.close()
    plot.wait()

def main():
    v0 = 2.0
    T = int(next(sys.stdin))
    for x in range(1, T+1):
        C, F, X = (float(x) for x in next(sys.stdin).split())
        t = Tf(v0, C, F, X)
#        plot(t, 10); return
        Ncur, Tcur = next(t)
        for Ni, Ti in t:
            if Ti > Tcur:
                print("Case #{}: {}".format(x, Tcur))
                break
            else:
                Tcur = Ti
                Ncur = Ni

if __name__ == '__main__':
    main()

