
#============================================

curProblem = "A";
curAttempt = 0;
curType = "example";
curType = "practice";
curType = "small";
curType = "large";

exampleString = """3
---+-++- 3
+++++ 4
-+-+- 4
""";

def getInput():
    if curType == "example": return exampleString;

    fileName = "%s-"%(curProblem);
    if curType == "large": fileName = "%s-large.in"%(curProblem);
    if curType == "small": fileName = "%s-small-attempt%d.in"%(curProblem,curAttempt);
    if curType == "practice": fileName = "%s-small-practice.in"%(curProblem);

    with open(fileName, "rt") as f:
        buf = f.readlines();

    return "".join(buf);

def parseInput(buf):
    buf = buf.split("\n");
    buf = filter(len,buf);

    outbuf = [];

    N = int(buf[0]);
    for x in buf[1:]:
        x = x.split();
        outbuf.append([x[0], int(x[1])]);
    return outbuf;

def solveProblem(rnd, x):
    ## Do actions
    
    S, K = x;
    
    print rnd;
    print S, K;
    
    opp = {"-" : "+", "+" : "-" };
    for n in xrange(1000000):
        mn = S.find("-");
        if mn < 0: return n;
        if mn + K - 1 >= len(S): return "IMPOSSIBLE";
        S = list(S);
        for ind in xrange(mn, mn+K):
            S[ind] = opp[S[ind]];
        S = "".join(S);
        print "After %d rounds: %s"%(n, S);

    return "IMPOSSIBLE";

#============================================

from time import time;

if __name__ == '__main__':
    inputData = parseInput(getInput());
    outfile = "%s.out"%(curProblem);

    start=time();
    with open(outfile,"wt") as f:
        for rnd, inp in enumerate(inputData):
            res = solveProblem(rnd, inp);
            st="Case #%d: %s\n"%(rnd+1,res);
            print st[:-1]; f.write(st);

    print "Total time: %fs"%(time()-start);

#============================================
