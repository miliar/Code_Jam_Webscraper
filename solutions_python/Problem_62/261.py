import pprint as pp

f = open('A-large.in')
rl = f.readline
T = int(rl())
for t_ in range(1,T+1):
    N = int(rl())
    x = [rl() for i in range(N)]
    x = [map(int, a.split()) for a in x]

    # x is a list of [a,b]'s
    # for each pair of wires [x,y], they intersect if
    # x.a-y.a is diff sign than x.b-y.b
    x.sort()
    ints = 0
    for i in range(N):
        this = x[i]
        for j in range(i):
            if x[j][1] > this[1]:
                ints += 1
    print 'Case #%d: %d' % (t_, ints)
