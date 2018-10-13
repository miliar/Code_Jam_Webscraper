from sys import stdin

T = int(stdin.readline())
for t in range(1, T+1):
    N = int(stdin.readline())
    wires = [map(int, stdin.readline().split()) for i in range(N)]
    wires.sort(key=lambda x: x[0])
    a_ranks = zip(range(N), wires)
    a_ranks.sort(key = lambda x: x[1][1])
    ab_ranks = zip(range(N), a_ranks)
    print "Case #%d: %d" % (t, sum(max(0, x[0] - x[1][0]) for x in ab_ranks))
