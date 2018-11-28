
def GCD(a, b):
    while b != 0:
        tmp = b
        b = a - b * (a/b)
        a = tmp
    return a


def DoIt(events):
    ans = abs(events[0]-events[1])
    if len(events) == 2:
        return (ans - (events[0]%ans))%ans
    
    for i in xrange(len(events)-1):
        ans = GCD(ans, abs(events[i] - events[i+1]))

    if ans == 1:
        return 0
    
    return (ans - (events[0]%ans))%ans

fin = open("B-large.in", 'r')
fout = open("B-large.out", 'w')

C = int(fin.readline().strip())

for c in xrange(C):
    e = map(int, fin.readline().strip().split())
    evs = list(set(e[1:]))
    fout.write("Case #%d: %d\n" % (c+1, DoIt(evs)))
    
