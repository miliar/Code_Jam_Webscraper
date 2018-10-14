# N = 1000
# h = 1


def f(N, h):
    k = 0
    su = 0

    while h > su:
        k += 1
        su = 2 * su + 1

    k = k - 1
    su = (su - 1) / 2

    p = (N - su) % 2**k
    s = (N - su) / 2**k
    m = h - su
    if m > p:
        t1, t2 = s - 1 - (s - 1) / 2, (s - 1) / 2
    else:
        t1, t2 = s - s / 2, s / 2

    return max(t1, t2), min(t2, t1)

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, m = [int(s) for s in raw_input().split(" ")]
  a, b = f(n, m)
  print "Case #{}: {} {}".format(i, a, b)