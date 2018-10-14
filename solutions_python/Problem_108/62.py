import sys

def solve(N, V, D):
    xd = [0] * len(V)
    xd[0] = V[0][0]

    for i in xrange(len(V)):
        #print xd
        if not xd[i]:
            return "NO"

        reach = V[i][0] + min(xd[i], V[i][1])
        if reach >= D:
            return "YES"

        for j in xrange(i+1, len(V)):
            if V[j][0] > reach:
                break
            if not xd[j]:
                xd[j] = V[j][0] - V[i][0]
    return "NO"


def RL():
    return map(int, sys.stdin.readline().split())

if __name__ == '__main__':
    NP = int(sys.stdin.readline())
    for i in xrange(NP):
        N, = RL()
        V = [tuple(RL()) for _ in xrange(N)]
        D, = RL()
        #print N,V,D
        print("Case #%d: %s" % (i+1, solve(N, V, D)))

