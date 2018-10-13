split_cache = {}
def divroundup(a, b):
    return a / b + (0 if a % b == 0 else 1)
def split_until(p, eat):
    if p <= eat:
        return 0
    leftovers = p - eat
    return divroundup(leftovers, eat)

def do_with_eating(pancakes, eat):
    import copy
    specials = 0
    for p in pancakes:
        specials += split_until(p, eat)
    return eat + specials

T = int(raw_input())
for test in range(T):
    D = int(raw_input())
    P = map(int, raw_input().split())
    #assert D == len(P)
    m = 100000

    for e in range(1, 1002):
        m = min(m, do_with_eating(P, e))
    print 'Case #%d: %d' % (test+1, m)

    
