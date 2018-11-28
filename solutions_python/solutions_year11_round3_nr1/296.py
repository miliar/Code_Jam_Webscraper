# -*- coding: utf-8 -*-
import sys
nfh = sys.argv[0][:-3];
nfhin = nfh + ".in"; nfhout= nfh + ".out";
fin = open(nfhin, "r"); fout= open(nfhout,"w");
def rl(): global fin; return fin.readline()[:-1];
def out(cnum, outs): global fout; fout.write("".join(["Case #",str(cnum),": ",str(outs),"\n"]));
def end(): global fout; fout.close();

# --- program ---
def title(t,i,j):
    t[i][j] = '/'
    c = 1
    try:
        if t[i][j+1] == "#":
            t[i][j+1] = '\\';
            c += 1
        if t[i+1][j+1] == "#":
            t[i+1][j+1] = '/'
            c += 1
        if t[i+1][j] == "#":
            t[i+1][j] = '\\'
            c += 1
        if c == 4: return 0, t
        return "Impossible", t
    except:
        return "Impossible", t
def pt(t):
    r = ""
    for i in t:
        r += "".join(i) + "\n"
    if r != "":
        r = "\n" + r[:-1]
    return r

def main(t):
    r = len(t)
    c = len(t[0])
    for i in xrange(r):
        for j in xrange(c):
            if t[i][j] == "#":
                res, t = title(t,i,j)
                if res != 0: return "\n" + res
    return pt(t)

# --- test configuration ---
NT = int(rl());
for T in xrange(1, NT+1):
    # Change the parameters here
    r,c = map(int, rl().split())
    t = []
    while r > 0:
        t.append([ x for x in rl()])
        r -= 1

    # Launch each test
    res = main(t)

    # Just output the result
    out(T,res)
end()
