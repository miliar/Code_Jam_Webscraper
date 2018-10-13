from fractions import gcd
with open("fair_warning_large.in","r") as fin: lines = fin.readlines()

C = int(lines[0])
with open("fair_warning_large.out","w") as fout:
    for i,line in enumerate(lines[1:]):
        tokens = map(int,line.split())
        N, ts = tokens[0],tokens[1:]
        assert len(ts) == N
        diffs = [abs(t1-t2) for (t1,t2) in zip(ts[1:],ts[:-1])]
        T = reduce(gcd,diffs)
        mint = min(ts)
        y = 0 if mint % T == 0 else T - (mint % T)
        fout.write("Case #%i: %i\n"%(i+1,y))