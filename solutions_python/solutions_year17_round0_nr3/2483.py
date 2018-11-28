debug_mode = False

def debug(*args):
    if debug_mode:
        print("DEBUG: ", end='')
        print(*args)

import itertools

def do_case(n, k):
    debug(n, k)
    p = 1
    s = [False] * (n + 2)
    s[0] = True
    s[n + 1] = True
    while p <= k:
        debug("PRE", s, p, k)
        ls = 0
        cand = None
        for ps in range(n + 2):
            if s[ps]:
                ls = 0
                continue
            rs = sum(1 for _ in itertools.takewhile(lambda a: not a, s[ps + 1:]))

            if cand is None:
                cand = (ps, ls, rs)
            elif min(ls, rs) > min(cand[1], cand[2]):
                cand = (ps, ls, rs)
            elif min(ls, rs) == min(cand[1], cand[2]) and max(ls, rs) > max(cand[1], cand[2]):
                cand = (ps, ls, rs)

            debug(p, ps, ls, rs, cand)
            ls = ls + 1
        p = p + 1
        s[cand[0]] = True
        debug("POST", p, cand, s)
    return "{0} {1}".format(max(cand[1], cand[2]), min(cand[1], cand[2]))

t = int(input())
q = 1
while q <= t:
    n, k = (int(i) for i in input().split())
    a = str(do_case(n, k))
    print("Case #{qno}: {ans}".format(qno=q, ans=a))
    q = q + 1
    
