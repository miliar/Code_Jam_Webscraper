import collections

src = open("C-small-attempt0.in", "r")
out = open("C-small-results.in", "w")

t = int(src.readline())

for i in range(1, t + 1):
    r, k, n = list(map(int, src.readline().split()))
    gg = list(reversed(list(map(int, src.readline().split()))))
    q = collections.deque(gg, maxlen=n)
    euros = 0

    for rr in range(r):
        fill = 0
        rotations = 0
        while fill + q[-1] <= k and rotations < n:
            fill += q[-1]
            rotations += 1
            q.rotate()
        euros += fill

    ans = "Case #{0}: {1}".format(i, euros)
    if i == t:
        out.write(ans)
    else:
        out.write(ans+'\n')

out.close()
