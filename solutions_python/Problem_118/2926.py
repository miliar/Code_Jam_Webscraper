#t = int(raw_input())

LIM = 40
RANGE = LIM*LIM
data = [0 for i in xrange(RANGE)]
true=True
false=False

def isPal(i):
    s = str(i)
    if s==s[::-1]:
        return true
    return false

sq=[]


for i in xrange(1, LIM):
    if isPal(i):
        if isPal(i*i):
            data[i*i]=1
            sq.append(i*i)


def low(a, i):
    left = 0
    right = len(sq)
    mid = 0
    while(left<right):
        mid = (right+left)/2
        if (a[mid]<i):
            left=mid+1
        else:
            right=mid
        print left,right,mid
    return left

print sq

f = open("input", "r").readlines()
g = open("output", "w")
t = int(f[0].strip())
for i in xrange(1, t+1):
    l = f[i].split()
    A = int(l[0].strip())
    B = int(l[1].strip())
    counter = 0
    for n in sq:
        if (n>=A and n<=B):
            counter+=1
    g.write("Case #%d: %d\n"%(i, counter))
