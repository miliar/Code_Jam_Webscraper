gcj alien language
system:sage

{{{id=8|
def onthaak(s,N):
    res = list(range(N))
    for cnt in range(N):
        res[cnt] = []
    cnt = 0
    inhaken = False
    for l in s:
        if l=='(':
            res[cnt]=[]
            inhaken=True
        elif l==')':
            cnt=cnt+1
            inhaken = False
        else:
            res[cnt].append(l)
            if not inhaken:
                cnt=cnt+1
    return res
///
}}}

{{{id=0|
f = open(DATA+'A-small.in','r')
lines=f.readlines()
f.close();
///
}}}

{{{id=15|
gegeven = lines[0].split()
L =int(gegeven[0])+0
D =int(gegeven[1])+0
N =int(gegeven[2])+0
///
}}}

{{{id=18|
woorden = lines[1:D+1]
letters = set()
for w in woorden:
    letters = letters.union(set(w))
///
}}}

{{{id=20|
lookup = list(range(L))
for i in range(L):
    d={}
    for l in letters:
        d[l]=[]
    for l in letters:
        for w in woorden:
            if w[i]==l:
                d[l].append(w)
    lookup[i]=d
///
}}}

{{{id=21|
outfile = open('problemalienlarge.out','w')
///
}}}

{{{id=22|
codes =lines[(D+1):(D+N+1)]
casenb = 1
for c in codes:
    resultset=set(woorden);
    oc = onthaak(c.strip(),L)
    nlc=0
    for lc in oc:
        subset = set()
        for ilc in lc:
            if ilc in letters:
                subset=subset.union(lookup[nlc][ilc])
        nlc=nlc+1
        resultset = resultset.intersection(subset)
    outfile.write('Case #'+str(casenb)+': '+str(len(resultset))+'\n')
    casenb = casenb+1
///
}}}

{{{id=6|
outfile.close()
///
}}}

{{{id=30|

///
}}}