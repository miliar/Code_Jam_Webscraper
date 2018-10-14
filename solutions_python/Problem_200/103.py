
#============================================

curProblem = "B";
curAttempt = 0;
curType = "example";
#curType = "practice";
#curType = "small";
curType = "large";

exampleString = """4
132
1000
7
111111111111111110
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
    for x in buf[1:]:
        outbuf.append(int(x));

    return outbuf;

def solveProblem(rnd, x):
    ## Do actions

    N = x;
    print rnd, N;

    v = map(int, list(str(N)));
    rst = "0"*len(v);
    for index in xrange(len(v)):
        for i in xrange(9,-1,-1):
            rst = rst[:index] + str(i)*(len(v)-index);
            if int(rst) <= N: break;
    return int(rst);

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
