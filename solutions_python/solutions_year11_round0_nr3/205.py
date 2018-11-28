
def doProb(fname, ofname):
    #do problem C given a file name
    f = open(fname, 'r');
    of = open(ofname, 'w');
    T = int(f.readline());

    output = ['Case #' + str(i) + ': '+ doStuff(int(f.readline()), [int(x) for x in f.readline().split()]) + '\n' for i in xrange(1,T+1)]
    f.close();      

    of.writelines(output);
    of.close();

def doStuff(N, vals):
    #tricky tricky but actually SO EASY!!!
    tot = 0;
    for v in vals:
        tot ^= v;
    if(tot !=0):
        return 'NO'
    else:
        return str(sum(vals)-min(vals))
        
            

pf = 'C:\\Python27\\gcj11\\qual\\C';
#doProb(pf + '\\csmall.in', pf + '\\csmall.out')
doProb(pf + '\\clarge.in', pf + '\\clarge.out')
#doProb(pf + '\\c.in', pf + '\\c.out')

