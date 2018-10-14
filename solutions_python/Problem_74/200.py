
def doProb(fname, ofname):
    #do problem A given a file name
    f = open(fname, 'r');
    T = int(f.readline());
    output = [];
    for xx in xrange(T):
        Line = f.readline().split();
        N = int(Line[0]);
        (total, freeB, freeO, b, o) = (N, 0, 0, 1, 1);
        for i in xrange(1,N+1):
            #print total, ', ', freeB, ', ', freeO, ', ', b, ', ', o
            np = int(Line[2*i]);
            if(Line[2*i-1] == 'B'):
                steps = max(0, abs(b-np)-freeB);
                total += steps;
                freeB = 0;
                freeO += steps+1;
                b = np;
            else:
                steps = max(0, abs(o-np)-freeO);
                total += steps;
                freeO = 0;
                freeB += steps+1;
                o = np;            
        output.append('Case #' + str(xx+1) + ': ' + str(total)+'\n');

    f.close();  
    of = open(ofname, 'w');
    of.writelines(output);
    of.close();   



pf = 'C:\\Python27\\gcj11\\qual\\A';

#doProb(pf + '\\asmall.in', pf + '\\asmall.out')
doProb(pf + '\\alarge.in', pf + '\\alarge.out')
#doProb(pf + '\\a.in', pf + '\\a.out')
