N = input()

def gcj1():
    P, K, L = (int(e) for e in raw_input().split())
    freqs = reversed(sorted([int(e) for e in raw_input().split()]))
    if L > P * K:
        return "IMPOSSIBLE"
    count = 0
    cur_num = 1
    i = 1
    for l in freqs:
        count += l * cur_num
        i += 1
        if i > K:
            i = 1
            cur_num += 1
    return count

for i in xrange(1, N + 1):
    print "Case #%d:" % i,
    print gcj1()
