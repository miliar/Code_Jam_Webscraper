from collections import defaultdict

cache = set()
def solve(keys, chests, opened):
    key = tuple(sorted(opened))
    if key in cache:
        return None
    if len(opened) == len(chests):
        return []
    for i, c in enumerate(chests):
        if i in opened:
            continue
        k = c[0]
        if keys[k] >= 1:
            keys[k] -= 1
            opened.add(i)
            for n in c[2:]:
                keys[n] += 1
            s = solve(keys, chests, opened)
            if s is not None:
                s.append(i+1)
                return s
            keys[k] += 1
            opened.remove(i)
            for n in c[2:]:
                keys[n] -= 1
    cache.add(key)
    return None
            
if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1,T+1):
        cache = set()
        K,N = [int(x) for x in raw_input().split()]
        keys = defaultdict(int)
        initial_keys = [int(x) for x in raw_input().split()]
        for k in initial_keys:
            keys[k] += 1
        chests = []
        for j in range(N):
            chests.append([int(x) for x in raw_input().split()])
        s = solve(keys, chests, set())
        if s is None:
            s = "IMPOSSIBLE"
        else:
            s = " ".join([str(a) for a in reversed(s)])
        print "Case #%d: %s" % (i, s)
        
            
