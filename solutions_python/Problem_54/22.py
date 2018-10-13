# Big num problems suck, yes they do, they absolutely do and
# I hope this is not ever, ever repeated.
import sys
import string

f = open( sys.argv[1] )
def getInt():
    return int(f.readline())
    

def getInts():
    x = string.split(f.readline(),' ')
    res = []
    for y in x :
        res.append(int(y))
    return res

def gcd(a,b):
    if( b == 0):
        return a
    return gcd(b, a%b)

def solve(vec):
    n = vec[0]
    T = abs(vec[1] - vec[2])
    i = 1
    while ( i <= n) :
        j = i+1
        while (j <= n) :
            #print "T = %d"%T 
            T = gcd(T, abs(vec[j]-vec[i]) )
            j += 1
        i += 1
    #print "T = %d"%T        
    return (T - vec[1]%T ) % T 
    
    


# read stuff:
C = getInt()
for i in range(1,C+1):
    vec = getInts()
    print "Case #%d: %d"%(i,solve(vec))   



