from sys import stdin

def get_best(a, b):
    n = len(a)
    used = set()
    score = n
    for i in xrange(0, n):
        lost = False
        for j in xrange(0, n):
            if b[j] > a[i] and b[j] not in used:
                used.add(b[j])
                score -= 1
                lost = True
                break
        if not lost:
            break
    return score

T = int(stdin.readline().rstrip())

for t in xrange(0, T):
    n = int(stdin.readline().rstrip())
    an = sorted([float(i) for i in stdin.readline().rstrip().split(" ")])
    ak = sorted([float(i) for i in stdin.readline().rstrip().split(" ")])

    print "Case #{}: {} {}".format(t+1, n-get_best(ak, an), get_best(an, ak))
