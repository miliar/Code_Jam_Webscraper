import string

infile = open('a.in','r')
outfile = open('a.out','w')

T = int(string.strip(infile.readline()))    

#returns 0 if cannot have max p
#returns 1 if can have max p
def analyze_no_surprise(num, p):
    (a,b) = (num/3,num%3)
    if a + (b>0) >= p:
        return 1
    return 0

def analyze_surprise(num,p):
    (a,b) = (num/3,num%3)
    if a + (b>0) >= p-1:
        if num > 1 and (not b==1) and num < 29:
            return 1
    return 0

for k in xrange(T):
    s = map(int,string.strip(infile.readline()).split())
    (N,S,p,t) = (s[0], s[1], s[2], s[3:])
    vals1 = map(lambda x:analyze_no_surprise(x,p), t)
    vals2 = map(lambda x:analyze_surprise(x,p),t)
    vals3 = map(lambda x,y: (x==0) and (y==1), vals1, vals2)
    answer = min(S, sum(vals3)) + sum(vals1)
    
    outfile.write('Case #%d: %s\n' % (k+1,answer))

