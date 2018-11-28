# -*- coding: utf-8 -*-
import sys
nfh = sys.argv[0][:-3];
nfhin = nfh + ".in"; nfhout= nfh + ".out";
fin = open(nfhin, "r"); fout= open(nfhout,"w");
def rl(): global fin; return fin.readline()[:-1];
def out(cnum, outs): global fout; fout.write("".join(["Case #",str(cnum),": ",str(outs),"\n"]));
def end(): global fout; fout.close();

# --- program ---
def main(a):
    lenv = len(a)
    i = 0
    curp = [1,1]
    PS = []
    tt = [-1,-1]
    M = [[],[]]
    while (lenv > 0):
        r = 0 if a[i] == "O" else 1
        b = int(a[i+1])
        PS.insert(0,(b,r))
        i += 2
        lenv -= 2
        M[r].insert(0,b)
    
    if len(M[0]) > 0:
        tt[0] = abs(curp[0] - M[0][-1]) + 1
        curp[0] = M[0][-1]
    if len(M[1]) > 0:
        tt[1] = abs(curp[1] - M[1][-1]) + 1
        curp[1] = M[1][-1]

    t = 0
    while len(PS) > 0:
        t += 1
        target = PS[-1]
        # print "T", t, "PRI:", target, "tt", tt, M
        if tt[0] > 0:
            tt[0] -= 1
        if tt[1] > 0:
            tt[1] -= 1
        
        if len(M[0]) > 0:
            if tt[0] == 0:
                # push time
                if target[0] == M[0][-1] and target[1] == 0:
                    PS.pop()
                    M[0].pop()
                    if len(M[0]) > 0:
                        tt[0] = abs(curp[0] - M[0][-1]) + 1
                        curp[0] = M[0][-1]
                else:
                    tt[0] += 1
    
        if len(M[1]) > 0:
            if tt[1] == 0:
                # push time
                if target[0] == M[1][-1] and target[1] == 1:
                    PS.pop()
                    M[1].pop()
                    if len(M[1]) > 0:
                        tt[1] = abs(curp[1] - M[1][-1]) + 1
                        curp[1] = M[1][-1]
                else:
                    tt[1] += 1

    return t

# --- test configuration ---
NT = int(rl());
for T in xrange(1, NT+1):
    param = rl()
    seq = param.split(" ")[1:]
    print T, seq
    res = main(seq)
    out(T,res)
end()
