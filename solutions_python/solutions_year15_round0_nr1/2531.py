import sys

def solve(c):
    print 'Case #%d:' % c,
    data = sys.stdin.readline().split()
    S_max = int(data[0])
    people = [int(p) for p in data[1]]

    friends = standing = 0

    for s in xrange(S_max+1):
        if people[s]:
            if standing >= s:
                standing += people[s]
            else:
                needed = s - standing
                standing += people[s] + needed
                friends += needed

    print friends


N = int(sys.stdin.readline())
for c in xrange(1, N+1):
    solve(c)
