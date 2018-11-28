
def doProb(fname, ofname):
    #do problem A given a file name
    f = open(fname, 'r');
    T = int(f.readline());
    output = [];
    for xx in xrange(T):        
        [R, C] = map(int, f.readline().split());        

        Pic = []
        for i in xrange(R):            
            Pic.append([c for c in f.readline().strip()])        
                
        output.append('Case #' + str(xx+1) + ':\n' + doStuff(Pic)+'\n');

    f.close();  
    of = open(ofname, 'w');
    of.writelines(output);
    of.close();   

def doStuff(Pic):
    R = len(Pic)
    C = len(Pic[0])
    for i in xrange(R):
        for j in xrange(C):
            if(Pic[i][j] == '#'):
                if(i>=R-1 or j>=C-1 or Pic[i+1][j]!='#' or Pic[i][j+1]!='#' or Pic[i+1][j+1]!='#'):
                    return 'Impossible'
                else:                
                    Pic[i][j] = '/'
                    Pic[i+1][j] = '\\'
                    Pic[i][j+1] = '\\'
                    Pic[i+1][j+1] = '/'
    Pic2 = ''
    for i in xrange(R):        
        for j in Pic[i]:            
            Pic2 = Pic2 + j    
        if(i<R-1):
            Pic2 = Pic2+ '\n'    
    return Pic2




pf = 'C:\\Python27\\gcj11\\Round1C\\A';

#doProb(pf + '\\asmall.in', pf + '\\asmall.out')
doProb(pf + '\\alarge.in', pf + '\\alarge.out')
#doProb(pf + '\\a.in', pf + '\\a.out')
