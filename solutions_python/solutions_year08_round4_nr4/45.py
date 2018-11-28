from math import sqrt
from math import pow

def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def xpermutations(items):
    return xcombinations(items, len(items))

def permute(S, a, k):
    r="";
    d=0;
    for i in range(len(S)):
        idx=d + a[i%k];
        #print i, d, idx;
        r +=S[idx];
        if ((i+1) % k == 0):
            d+=k;
    #print S, r;
    return r;


def solve(k,S):
    print k,S;
    m=len(S)+1;
    for p in xpermutations(range(k)):
        pp = permute(S, p, k);
        pprle=rle(pp);
        if (pprle < m):
            m = pprle;
        #print p, pp, pprle;
    return m;

def rle(S):
    cnt = 1;
    for i in range(len(S)-1):
        if (S[i] != S[i+1]):
            cnt += 1;
    print S, cnt;
    return cnt;
   
def solveAll():
    name="D-small-attempt0";
    
    fi=open("C:/" + name + ".in", "r");
    fo=file("C:/" + name + ".out", "w");

    n=int(fi.readline());
    print "n", n;
    
    for i in range(n):
        #print "i",i;

        #r1=int(fi.readline());
        #print "r1", r1;
        k=int(fi.readline());
        S=fi.readline().rstrip();
        
        rez=solve(k,S);
        rezs=str(rez);

        #print "rez", rez;
        #print "rezs", rezs;
           
        rezString="Case #%s: %s\n" % ((i+1), rezs);
        print rezString;
        fo.write(rezString);

    fo.close();


solveAll()

#rle("aabcaaaa");
#rle("a");
#rle("ab");
#print range(4);
#for p in xpermutations(range(5)): print p;
#permute("abcdef", range(3), 3);
for p in xpermutations(range(16)): print "";
