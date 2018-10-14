def solve(v1, v2):
    r = []
    for i in range(len(v1)):
        x = min(v1)
        v1.remove(x)
        y = max(v2)
        v2.remove(y)
        r.append((x,y))
    return reduce(lambda x,y: x+y, map(lambda v: v[0] * v[1], r))

def read_input():
    from sys import stdin
    N = int(stdin.readline())
    for n in range(N):
        stdin.readline()
        vetor1 = map(int, stdin.readline().split())
        vetor2 = map(int, stdin.readline().split())
        print "Case #%d: %d" % (n+1, solve(vetor1, vetor2))

read_input()
