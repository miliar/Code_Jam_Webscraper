
#============================================

curProblem = "C";
curAttempt = 1;
curType = "example";
#curType = "practice";
#curType = "small";
curType = "large";

exampleString = """5
4 2
5 2
6 2
1000 1000
1000 1
857120 660988
822711284578373888 308268242481988352
""";

def getInput():
    if curType == "example": return exampleString;

    fileName = "%s-"%(curProblem);
    if curType == "large": fileName = "%s-large.in"%(curProblem);
    if curType == "small": fileName = "%s-small-2-attempt%d.in"%(curProblem,curAttempt);
    if curType == "practice": fileName = "%s-small-practice.in"%(curProblem);

    with open(fileName, "rt") as f:
        buf = f.readlines();

    return "".join(buf);

def parseInput(buf):
    buf = buf.split("\n");
    buf = filter(len,buf);

    outbuf = [];
    for x in buf[1:]:
        outbuf.append(map(int, x.split(" ")));

    return outbuf;

def solveProblem(rnd, x):
    ## Do actions

    def sortRoutine(a,b):
        v = cmp(a[0], b[0]);
        if v != 0: return -v;
        return cmp(a[1], b[1]);

    N,K = x;
    arr = { N:1 };
    while True:
        rng = max(arr.keys());
        count = arr[rng];
        K -= count;
        del arr[rng];

        newIndex = (rng - 1) // 2;
        L = newIndex;
        R = rng - 1 - newIndex;

        if L > 0:
            try: arr[L] += count;
            except: arr[L] = count;
        if R > 0:
            try: arr[R] += count;
            except: arr[R] = count;

        if K <= 0: break;

    return "%s %s"%(max(L,R), min(L,R));

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
