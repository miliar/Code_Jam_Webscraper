
#============================================

parallel = False;
parallel = True;
curProblem = "A";
curAttempt = 0;
curType = "example";
#curType = "practice";
curType = "small";
#curType = "large";

exampleString = """3
3 3
G??
?C?
??J
3 4
CODE
????
?JAM
2 2
CA
KE
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

    outBuf = [];
    T = int(buf[0]); buf=buf[1:];
    for _ in xrange(T):
        R, C = map(int, buf[0].split(" ")); buf = buf[1:];
        arr = [ list(x[:]) for x in buf[:R] ];
        buf = buf[R:];
        outBuf.append([ R, C, arr ]);
    return outBuf;

def isValid(arr, R, C):
    used = [ [0]*C for _ in xrange(R) ];
    usedChar = set([]);
    #print "ARR = %s"%(arr);
    for r in xrange(R):
        for c in xrange(C):
            if used[r][c] == 1: continue;
            if arr[r][c] in usedChar: return False;
            width = height = 1;
            for _c in xrange(c+1,C):
                if arr[r][_c] != arr[r][c]: break;
                width += 1;
            for _r in xrange(r+1,R):
                if arr[_r][c] != arr[r][c]: break;
                height += 1;
            #print "(%d,%d) + (%d,%d) = %s"%(r,c,width,height,arr[r][c]);
            maxR = min(R, r+height);
            maxC = min(C, c+width);
            if any( arr[_r][_c]!=arr[r][c] for _r in xrange(r, maxR) for _c in xrange(c, maxC) ):
                return False;
            #print "(%d,%d) + (%d,%d) = %s"%(r,c,width,height,arr[r][c]);
            for _r in xrange(r, maxR):
                for _c in xrange(c, maxC):
                    used[_r][_c] = 1;
            usedChar.add(arr[r][c]);
    return True;

def rec(index, R, C, arr, chars):
    if index < 0:
        return isValid(arr,R,C), arr;

    r, c = index // C, index % C;
    if arr[r][c] != '?': return rec(index-1, R, C, arr, chars);
    narr = [ arr[_r][:] for _r in xrange(R) ];
    for v in chars:
        narr[r][c] = v;
        ret, retArr = rec(index-1, R, C, narr, chars);
        if ret == True: return True, retArr;
    return False, None;

def solveProblem(rnd, x):
    ## Do actions

    R, C, arr = x;
    #print arr;

    chars = set();
    for row in arr:
        for x in row: chars.add(x);
    chars -= set(["?"]);

    ret, retArr = rec(R*C-1, R, C, arr, chars);
    if ret == False:
        print "INVALID";
        exit(0);

    st = "\n".join( "".join(x) for x in retArr );

    #stdout.flush();
    #exit(0);
    return "\n" + st;

def iterateProblems(f, inputData):
    from multiprocessing import Pool;

    pool = Pool(1) if parallel == False else Pool();
    resList = [ pool.apply_async(solveProblem, [rnd, inp]) for rnd, inp in enumerate(inputData) ];
    #resList = [ pool.apply(solveProblem, [rnd, inp]) for rnd, inp in enumerate(inputData) ];
    #resList = [ solveProblem(rnd, inp) for rnd, inp in enumerate(inputData) ];
    for rnd, res in enumerate(resList):
        res = res.get();
        st="Case #%d:%s\n"%(rnd+1,res);
        print st[:-1]; f.write(st);
        stdout.flush();

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
