
def doProb(fname, ofname):
    #do problem D given a file name


    
    f = open(fname, 'r');    
    of = open(ofname, 'w');
    T = int(f.readline());

    output = ['Case #' + str(i) + ': '+ doStuff(int(f.readline()), [int(x) for x in f.readline().split()]) + '\n' for i in xrange(1,T+1)]

    f.close();      

    of.writelines(output);
    of.close();

def doStuff(N, vals):
    #idea is to obtain cyclic structure and reduce each cycle independently
    z = [(vals[i],i) for i in xrange(N)];
    z.sort();
    prm = [i[1] for i in z]; #the permutation    
    marked = [False]*len(prm);
    cyc = []; #cycle structure
    for i in xrange(len(prm)):
        if(not(marked[i])):
            marked[i]=True;
            sz = 1;
            j = prm[i];            
            while(j!=i):
                marked[j] = True;
                j = prm[j];                
                sz+=1;                
            cyc.append(sz);
    cyc.sort();
    return str(getValue(cyc));

def getValue(cyc):
    #get the expected number of swaps for a group of cycles
    #taking a stab here...
    sm = 0;
    for i in cyc:
        if(i != 1):
            sm += i+0.000000;
    return sm



pf = 'C:\\Python27\\gcj11\\qual\\D';
#doProb(pf + '\\dsmall.in', pf + '\\dsmall.out')
doProb(pf + '\\dlarge.in', pf + '\\dlarge.out')
#doProb(pf + '\\d.in', pf + '\\d.out')

