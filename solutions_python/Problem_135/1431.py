from sys import stdin

T = int(stdin.readline().rstrip())

for t in xrange(0, T):
    grid1 = []
    grid2 = []
    a1 = int(stdin.readline().rstrip())
    for i in xrange(0, 4):
        grid1.append([int(n) for n in stdin.readline().rstrip().split(" ")])
    a2 = int(stdin.readline().rstrip())
    for i in xrange(0, 4):
        grid2.append([int(n) for n in stdin.readline().rstrip().split(" ")])

    x = set(grid1[a1-1])
    y = set(grid2[a2-1])
    z = x.intersection(y)
    if len(z) == 0:
        print "Case #{}: Volunteer cheated!".format(t+1)
    elif len(z) > 1:
        print "Case #{}: Bad magician!".format(t+1)
    else:
        print "Case #{}: {}".format(t+1, tuple(z)[0])
