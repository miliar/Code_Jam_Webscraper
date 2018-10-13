from queue import PriorityQueue


def expand_state(hd, ad, hk, ak, b, d, hdo):
    return [(hd - (ak if hk - ad > 0 else 0), ad, hk - ad, ak, b, d, hdo),  # attack
            (hd - (ak if hk > 0 else 0), ad + b, hk, ak, b, d, hdo),  # buff
            (hdo - (ak if hk > 0 else 0), ad, hk, ak, b, d, hdo),  # cure
            (hd - (max(0, ak - d) if hk > 0 else 0), ad, hk, max(0, ak - d), b, d, hdo)   # debuff
    ]


def heur(state):
    hd, ad, hk, ak, b, d, hdo = state
    return 0, state


def win(s):
    hd, ad, hk, ak, b, d, hdo = s
    return hd > 0 >= hk


def a_star(pq: PriorityQueue):
    cache = set()
    while not pq.empty():
        s = pq.get()
        state = s[1][1:]
        if win(state):
            return s[1][0]
        if state in cache:
            continue
        cache.add(state)
        nxt = map(heur, filter(lambda x: x[0] > 0, expand_state(*state)))
        for n in nxt:
            pq.put((n[0] + s[0] + 1, (s[0] + 1, *n[1])))
    return 'IMPOSSIBLE'


t = int(input())
for case in range(1, t + 1):
    hd, ad, hk, ak, b, d = map(int, input().split())
    pq = PriorityQueue()
    pq.put((0, (0, hd, ad, hk, ak, b, d, hd)))
    print('Case #{}: {}'.format(case, a_star(pq)))
