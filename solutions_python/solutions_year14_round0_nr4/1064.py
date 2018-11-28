
def check_opt(l1, l2):
    i1 = 0
    i2 = 0
    rv = 0
    while i1 < len(l1) and i2 < len(l2):
        while l1[i1] < l2[i2]:
            i1 += 1
            if i1 >= len(l1):
                return rv
        rv += 1
        i1 += 1
        i2 += 1
    return rv

def process_game():
    N = int(raw_input())
    b1 = sorted(map(float, raw_input().split()))
    assert(len(b1) == N)
    b2 = sorted(map(float, raw_input().split()))
    assert(len(b2) == N)
    print check_opt(b1, b2), N - check_opt(b2, b1)

for i in xrange(1, int(raw_input()) + 1):
    print "Case #%d:" % (i),
    process_game()
