f = open('A-large.in')

t = int(f.readline())

def plu(x,y):
    return x+y

for i in range(t):
    n = int(f.readline())

    a = map(int,f.readline().split(' '))
    b = map(int,f.readline().split(' '))
    a.sort()
    b.sort(reverse = True)

    ab = reduce(plu,map(lambda x:x[0]*x[1], zip(a,b)))

    print 'Case #%d: %d' % (i+1, ab)
