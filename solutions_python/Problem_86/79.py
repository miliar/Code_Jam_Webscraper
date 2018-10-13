
def doProb(fname, ofname):
    #do problem C given a file name
    f = open(fname, 'r');
    of = open(ofname, 'w');
    T = int(f.readline());

    output = ['Case #' + str(i) + ': '+ doStuff(map(int,f.readline().split()), map(int, f.readline().split())) + '\n' for i in xrange(1,T+1)]    

    f.close();      

    of.writelines(output);
    of.close();

def doStuff(NLH, freq):
    #Brute force for the moment
    [N, L, H] = NLH
    print N, L, H
    for test in xrange(L, H+1):
        p = True
        for j in freq:            
            if(j%test != 0 and test%j != 0):
                p = False
                break        
        if(p == True):            
            return str(test)
    return 'NO'
            
            

pf = 'C:\\Python27\\gcj11\\Round1C\\C';
doProb(pf + '\\csmall.in', pf + '\\csmall.out')
#doProb(pf + '\\clarge.in', pf + '\\clarge.out')
#doProb(pf + '\\c.in', pf + '\\c.out')

