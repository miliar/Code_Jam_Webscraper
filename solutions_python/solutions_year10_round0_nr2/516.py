'''
Created on May 7, 2010

@author: john
'''

def gcd(a,b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

fname=r"c:\Users\john\Downloads\B-small-attempt1"
fin = open(fname+".in")
fout = open(fname+".out","w")
T=int(fin.readline())

for t in xrange(T):
    l = sorted(map(int, fin.readline().split(" "))[1:])
    delta = [l[i+1]-l[i] for i in xrange(len(l)-1)]
    d = reduce(gcd,delta)
    fout.write("Case #%d: %d\n" % (t+1,d-l[0]%d if l[0]%d >1 else 0))
