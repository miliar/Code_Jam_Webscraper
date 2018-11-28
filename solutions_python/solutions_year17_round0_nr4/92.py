
#============================================

curProblem = "D";
curAttempt = 1;
curType = "example";
#curType = "practice";
curType = "small";
#curType = "large";

exampleString = """3
2 0
1 1
o 1 1
3 4
+ 2 3
+ 2 1
x 3 1
+ 2 2
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
    T = int(buf[0]); buf=buf[1:];
    for _ in xrange(T):
        N, M = map(int, buf[0].split(" ")); buf = buf[1:];
        lst = {};
        for _ in xrange(M):
            sym, R, C = buf[0].split(" "); buf = buf[1:];
            R, C = map(int, [R,C]);
            lst[R-1,C-1] = sym;
        outbuf.append([N, lst]);

    return outbuf;

def isValid(vals):
    items = sorted(vals.items());
    for i in xrange(len(items)):
        r0, c0 = items[i][0];
        s0 = items[i][1];
        for j in xrange(i+1, len(items)):
            r1, c1 = items[j][0];
            s1 = items[j][1];

            if r0 == r1 or c0 == c1:
                if s0 != "+" and s1 != "+": return False;
            if r0 + c0 == r1 + c1 or r0 - c0 == r1 - c1:
                if s0 != "x" and s1 != "x": return False;
    return True;

def solveProblem(rnd, x):
    ## Do actions

    N, lst = x;

    score = { "+":1, "x":1, "o":2 };
    def display(vals):
        arr = [ ["."]*N for _ in xrange(N) ];
        for k,v in vals.items(): arr[k[0]][k[1]]=v;
        print getTotal(vals), vals;
        for x in arr: print "".join(x);
        print;

    def getTotal(vals):
        total = 0;
        for v in vals.values(): total += score[v];
        return total;

    vals = { };
    oSpot = -1;
    for i in xrange(N):
        k = (0,i);
        if k in lst.keys():
            if lst[k] != "+": oSpot = i;
            vals[k] = lst[k];
        else: vals[k] = "+";

    if oSpot == -1: oSpot = 0;
    vals[0, oSpot] = "o";

    if oSpot != N-1:
        for r in xrange(oSpot): vals[r+1,r] = "x";
        for r in xrange(oSpot+1,N): vals[r,r] = "x";
    elif N > 1:
        vals[N-1,0] = "x";
        for r in xrange(1,oSpot): vals[r,r] = "x";

    for r in xrange(1,N-1): vals[N-1,r] = "+";

    total = getTotal(vals);
    arr = [];
    for k, v in vals.items():
        if k not in lst.keys() or lst[k] != v:
            arr.append("%s %s %s"%(v, k[0]+1, k[1]+1));
    st = "%d %d"%(total, len(arr));
    if len(arr) > 0: st = "%s\n%s"%(st, "\n".join(arr));
    return st;

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
