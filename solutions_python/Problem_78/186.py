from __future__ import division
import sys
nfh = sys.argv[0][:-3];
nfhin = nfh + ".in"; nfhout= nfh + ".out";
fin = open(nfhin, "r"); fout= open(nfhout,"w");
def rl(): global fin; return fin.readline()[:-1];
def out(cnum, outs): global fout; fout.write("".join(["Case #",str(cnum),": ",str(outs),"\n"]));
def end(): global fout; fout.close();

# --- program ---
def main(N, pd, pg):
    if pg == 100 and pd != 100: return "Broken"
    if pg == 0 and pd != 0: return "Broken"
    if pd == 100: return "Possible"

    i = 1
    while i <= N:
        div = i*pd/100
        i+=1
        if div == int(div): return "Possible"
    return "Broken"

# --- test configuration ---
NT = int(rl());
for T in xrange(1, NT+1):
    # Change the parameters here
    N, pd, pg  = map(int, rl().split())
    
    # Launch each test
    res = main(N,pd,pg)

    # Just output the result
    out(T,res)
end()
