from math import sqrt
from math import pow


def solve(P,K,L,fr):
    #print "solve",P,K,L,fr;
    fr.sort();
    fr.reverse();

    rez=0;
    press=1;
    cnt=0;
    for key in fr:
        if (press>P):
            rez=-1;
            break;
        rez+=key*press;
        cnt+=1;
        if (cnt % K == 0):
            press+=1;
        
    #print fr;
    #print rez;
    return rez;

   
def solveAll():
    name="A-large";
    
    fi=open("C:/" + name + ".in", "r");
    fo=file("C:/" + name + ".out", "w");

    n=int(fi.readline());
    print "n", n;
    
    for i in range(n):
        #print "i",i;
        r1=fi.readline();
        r2=fi.readline();
        #print "r1", r1;
        #print "r2", r2;
        
        x1=[int(xx) for xx in r1.rstrip().split(" ")];
        x2=[int(xx) for xx in r2.rstrip().split(" ")];
        #print x1, x2;
        [P,K,L]=x1;
        freq=x2;
        #print P,K,L;
        #print freq;

        rez=solve(P,K,L,freq);
        rezs=str(rez);
        if (rez==-1):
            rezs="Impossible";
        #print "rez", rez;
        #print "rezs", rezs;
           
        rezString="Case #%s: %s\n" % ((i+1), rezs);
        print rezString;
        fo.write(rezString);

    fo.close();


solveAll()



