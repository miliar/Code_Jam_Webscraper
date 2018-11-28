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
    a = sorted(a) 
    xor = 0
    for x in a:
        xor ^= x
    if xor != 0:
        return "NO"
    else:
        return sum(a) - min(a)

# --- test configuration ---
NT = int(rl());
for T in xrange(1, NT+1):
    rl()
    param = rl()
    res = main(map(int,param.split(" ")))
    out(T,res)
end()
