
#============================================

parallel = False;
#parallel = True;
curProblem = "C";
curAttempt = 0;
curType = "example";
#curType = "practice-small";
#curType = "practice-large";
curType = "small";
#curType = "large";

exampleString = """3
3 1
2 3
2 4
4 4
-1 1 -1
-1 -1 1
-1 -1 -1
1 3
4 1
13 10
1 1000
10 8
5 5
-1 1 -1 -1
-1 -1 1 -1
-1 -1 -1 10
-1 -1 -1 -1
1 4
4 3
30 60
10 1000
12 5
20 1
-1 10 -1 31
10 -1 10 -1
-1 -1 -1 10
15 6 -1 -1
2 4
3 1
3 2
""";

def getInput():
    if curType == "example": return exampleString;

    fileName = "%s-"%(curProblem);
    if curType == "large": fileName = "%s-large.in"%(curProblem);
    if curType == "small": fileName = "%s-small-attempt%d.in"%(curProblem,curAttempt);
    if curType == "practice-small": fileName = "%s-small-practice.in"%(curProblem);
    if curType == "practice-large": fileName = "%s-large-practice.in"%(curProblem);

    with open(fileName, "rt") as f:
        buf = f.readlines();

    return "".join(buf);

def iterateProblems(f, inputData):
    from multiprocessing import Pool;

    pool = Pool(1) if parallel == False else Pool();
    if parallel: resList = [ pool.apply_async(solveProblem, [rnd, inp]) for rnd, inp in enumerate(inputData) ];
    else:        resList = [ solveProblem(rnd, inp) for rnd, inp in enumerate(inputData) ];
    for rnd, res in enumerate(resList):
        if parallel: res = res.get();
        st="Case #%d: %s\n"%(rnd+1,res);
        print st[:-1]; f.write(st);
        stdout.flush();

def parseInput(buf):
    buf = buf.split("\n");
    buf = filter(len,buf);

    outBuf = [];
    T = int(buf[0]); buf=buf[1:];
    for _ in xrange(T):
        N, Q = map(int, buf[0].split()); buf=buf[1:];
        arrH = [];
        for _ in xrange(N): arrH.append(map(int, buf[0].split())); buf=buf[1:];
        arrD = [];
        for _ in xrange(N): arrD.append(map(int, buf[0].split())); buf=buf[1:];
        arrT = [];
        for _ in xrange(Q): arrT.append(map(int, buf[0].split())); buf=buf[1:];
        outBuf.append([N, Q, arrH, arrD, arrT]);
    return outBuf;

def solveProblem(rnd, x):
    ## Do actions
    N, Q, arrH, arrD, arrT = x;
    print x;
    stdout.flush();
    
    horseInfo = [[0, arrH[0][0], 0.0]];
    for city in xrange(1, N):
        dist = arrD[city-1][city];
        for info in horseInfo:
            horseID, horseDur, horseTime = info;
            speed = arrH[horseID][1];
            info[1] -= dist;
            info[2] += 1.0 * dist / speed;
        horseInfo = [ x for x in horseInfo if x[1] >= 0 ];
        bestTime = min(x[2] for x in horseInfo);
        if city == N-1: break;

        horseInfo.append([ city, arrH[city][0], bestTime ]);
        print "\tCity %d, horses = %s"%(city, horseInfo);

    print "\tBEST TIME: %s"%(bestTime);

    stdout.flush();
    return bestTime;

#============================================

from time import time;
from sys import stdout;

if __name__ == '__main__':
    inputData = parseInput(getInput());
    outfile = "%s.out"%(curProblem);

    start=time();
    with open(outfile,"wt") as f: iterateProblems(f, inputData);
    print "Total time: %fs"%(time()-start);

#============================================
