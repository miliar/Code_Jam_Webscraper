import string

infile = open('a.in','r')
outfile = open('a.out','w')

T = int(string.strip(infile.readline()))    

def to_list(n):
    out = []
    while(n>0):
        out.append(n%10)
        n /= 10
    out.reverse()
    return out

def shift(a):
    temp = a[0]
    out = a[1:]
    out.append(temp)
    return out

for k in xrange(T):
    s = map(int,string.strip(infile.readline()).split())
    A,B = s[0],s[1]
    answer = 0
    for i in range(A,B):
        lower = to_list(i)
        upper = lower[:]
        taken = set([])
        for j in range(len(lower)-1):
            upper = shift(upper)
            if lower < upper and upper <= to_list(B):
                taken.add(repr(upper))
        answer += len(taken)
    outfile.write('Case #%d: %s\n' % (k+1,answer))

