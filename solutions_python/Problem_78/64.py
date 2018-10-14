import string

infile = open('a.in','r')
outfile = open('a.out','w')

#assume a <= b
def gcd(a,b):
    if a == 0 or b == 0:
        return max(a,b)
    return gcd(min(a,b), max(a,b) % min(a,b))

def reduce_frac(a,b):
    return (a/gcd(a,b),b/gcd(a,b))

T = int(string.strip(infile.readline()))

for k in xrange(T):
    s = map(int,string.split(string.strip(infile.readline())))
    N = s[0]
    P_D = s[1]
    P_G = s[2]
    print s

    looks_good = True
    (a,b) = reduce_frac(P_D,100)
    print a,b
    if b > N:
        looks_good = False
    if P_G == 100 or P_G == 0:
        looks_good = P_D == P_G
    
    if looks_good:
        answer = "Possible"
    else:
        answer = "Broken"

    outfile.write('Case #%d: %s\n' % (k+1,answer))

