from sys import stdin

def each_case(people):
    stand, friend = 0, 0
    for s, p in enumerate(people):
        if s > stand:
            friend += (s - stand)
            stand = s
        stand += p
    return friend

T = int(stdin.readline())
for t in xrange(1,T+1):
    Smax, people = stdin.readline().split()
    people = map(int, people[:int(Smax)+1])
    print 'Case #{}: {}'.format(t, each_case(people))
