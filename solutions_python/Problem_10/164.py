def plu(x,y):
    return x+y

f = open('A-large.in')

n = int(f.readline())

for i in range(n):
    p,k,l = map(int,f.readline().split(' '))
    freq = map(int,f.readline().split(' '))
    freq.sort(reverse=True)

    s = 0
    t = 1
    while freq:
        s = s + t*reduce(plu,freq[:k])
        freq = freq[k:]
        t = t + 1


    print 'Case #%d: %d' % (i+1, s)
