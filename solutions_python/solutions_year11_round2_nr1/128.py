
def doProb(fname, ofname):
    #do problem A given a file name
    f = open(fname, 'r');
    T = int(f.readline());
    output = [];
    for xx in xrange(T):
        N = int(f.readline());
        L = [];
        for i in xrange(N):
            Line = f.readline().strip();
            L.append([])
            for j in xrange(N):
                val = 1 if Line[j]=='1' else (-1 if Line[j]=='0' else 0)
                L[i].append(val)

        scores = doStuff(N, L)
        output.append("Case #" + str(xx+1) + ':\n');
        for i in xrange(N):
            output.append(str(scores[i]) + '\n')        

    f.close();  
    of = open(ofname, 'w');
    of.writelines(output);
    of.close();   

def doStuff(N, L):
    #compute the RPI etc
    wp = []
    owp = []
    for i in xrange(N):
        wp.append(getWP(L, i))
        owp.append(getOWP(L, i))

    oowp = [];
    for i in xrange(N):
        oowp.append(getOOWP(L, i, owp))


##    print 'wp: ', wp
##    print 'owp: ', owp
##    print 'oowp: ', oowp
    total = []
    for i in xrange(N):
        total.append(0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i])
    return total

def getOOWP(L, k, owp):
    tot = 0
    owptot = 0
    x = L[k]
    for t in xrange(len(x)):
        i = x[t]
        if(i!=0):
            owptot += owp[t]
            tot +=1
    return owptot/float(tot)
            
    
def getOWP(L, k):
    x = L[k]
    tot = 0
    wptot = 0
    for t in xrange(len(x)):
        i = x[t]
        if(i!=0):
            wptot += getWP(L, t, k)
            tot +=1
    return wptot/float(tot)    

def getWP(L, k, excl = -1):
    x = L[k]
    tot = 0;
    nw = 0;
    for t in xrange(len(x)):
        i = x[t]
        if(t==excl):
            continue
        if(i!=0):
            tot +=1;
            if(i==1):
                nw +=1;
    return float(nw)/float(tot);


pf = 'C:\\Python27\\gcj11\\Round1B\\A';

#doProb(pf + '\\asmall.in', pf + '\\asmall.out')
doProb(pf + '\\alarge.in', pf + '\\alarge.out')
#doProb(pf + '\\a.in', pf + '\\a.out')
