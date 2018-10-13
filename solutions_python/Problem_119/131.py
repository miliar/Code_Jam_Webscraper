
import itertools

def update(D, k, v):
    if k not in D: D[k] = 0
    D[k] += v

def solve(N, keys, C_take, C_give):
    state_map = {}
    for mask in xrange(2**N):
        state = dict(keys)
        for bit in xrange(N):
            if mask & (1 << bit):
                update(state, C_take[bit + 1], -1)
                for v in C_give[bit + 1]:
                    update(state, v, 1)
        if any(x < 0 for x in state.itervalues()):
            state = None
        state_map[mask] = state

    def check(mask, key):
        state = state_map[mask]
        return state and state.get(key, 0) > 0

    path_map = {0: []}
    for nbits in xrange(1, N + 1):
        index = range(N)
        for pos in itertools.combinations(index, nbits):
            mask = sum(1 << p for p in pos)
            best, rest = None, None
            for p in pos:
                mask2 = mask ^ (1 << p)
                path = path_map[mask2]
                if path is None: continue
                if not check(mask2, C_take[p + 1]): continue
                if best is None or path < best:
                    best, rest = path, [p + 1]
            path_map[mask] = best + rest \
                if best is not None else None

    result = path_map[2**N-1]
    return ' '.join(map(str, result)) if result else 'IMPOSSIBLE'

def main(f):
    T = int(f.readline())
    for i in xrange(T):
        K, N = map(int, f.readline().split(' '))
        keys = {}
        for n in map(int, f.readline().split(' ')):
            if n not in keys: keys[n] = 0
            keys[n] += 1
        C_take, C_give = {}, {}
        for j in xrange(N):
            a = map(int, f.readline().split(' '))
            C_take[j + 1] = a[0]
            C_give[j + 1] = a[2:]
        print 'Case #%d:' % (i + 1), solve(N, keys, C_take, C_give)

if __name__ == '__main__':
    import sys
    main(sys.stdin)
