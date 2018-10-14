
#============================================

parallel = False;
#parallel = True;
curProblem = "B";
curAttempt = 2;
curType = "example";
#curType = "practice-small";
#curType = "practice-large";
curType = "small";
#curType = "large";

exampleString = """4
6 2 0 2 0 2 0
3 1 0 2 0 0 0
6 2 0 1 1 2 0
4 0 0 2 0 0 2
""";

exampleString = """1
558 144 0 265 0 149 0
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
        N, R, O, Y, G, B, V = map(int, buf[0].split()); buf=buf[1:];
        outBuf.append([N,R,O,Y,G,B,V]);
    return outBuf;

def solveProblem(rnd, x):
    ## Do actions

    N, R, O, Y, G, B, V = x;
    print x;
    stdout.flush();

    N = R+O+Y+B;

    def isMatch(a,b):
        if a == b: return True;
#        if a == 0 and (b == 5 or b == 1): return True;
#        elif a == 5 and (b == 4 or b == 0): return True;
#        elif b == a - 1 or b == a + 1: return True;
        return False;

    colorMap = "RYB";

    st = [];
    colors = [ [R,0], [Y,1], [B,2] ];
    for curHorse in xrange(N):
        colors = [ x for x in colors if x[0] > 0 ];
        colors.sort(reverse=True);
        validColors = [ x for x in colors if x[0] > 0 and (len(st)==0 or st[-1]!=x[1]) ];
        if len(validColors) == 0:
            return "IMPOSSIBLE";
#            for i in xrange(curHorse-2,0,-1):
#                if st[curHorse-1] == st[i-1]: continue;
#                if st[i] == st[curHorse-1]: continue;
#                preSt = st[:i];
#                postSt = list(reversed(st[i:]));
#                st = preSt + postSt;
#                #print st;
#                break;
#            else: return "IMPOSSIBLE";

        st.append(validColors[0][1]);
        validColors[0][0] -= 1;
        #print "st = %s, new index = %s"%(st, curIndex);

    if len(st) > 1 and st[0] == st[-1]:
        print "BAD LOOP";
        for i in xrange(N-1,0,-1):
            if st[N-1] == st[i-1]: continue;
            if st[i] == st[0]: continue;
            preSt = st[:i];
            postSt = list(reversed(st[i:]));
            st = preSt + postSt;
            #print st;
            break;
        else:
            return "IMPOSSIBLE";

        pass;

    ret = "".join(colorMap[x] for x in st);
    print ret;
    stdout.flush();
    return ret;
    

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
