import sys


def solve(r, o, y, g, b, v):
    '''Solve the small dataset...'''
    assert(o == 0 and g == 0 and v == 0)

    sorted_unicorns = list(sorted(zip([r,y,b], 'RYB')))
    mapping = dict(zip('ABC', (x[1] for x in sorted_unicorns)))
    unicorns = dict(zip('ABC', (x[0] for x in sorted_unicorns)))
    #print(unicorns, file=sys.stderr)
    #print(mapping, file=sys.stderr)
    u = max((unicorns[x], x) for x in unicorns.keys())
    ans = u[1]
    unicorns[u[1]] -= 1
    while max(unicorns.values()) > 0:
        #print(unicorns, file=sys.stderr)
        u = max((unicorns[x], x) for x in unicorns.keys() if x != ans[-1])
        if u[0] <= 0:
            return 'IMPOSSIBLE'
        ans += u[1]
        unicorns[u[1]] -= 1
    #print(len(ans), file=sys.stderr)
    #print(r+y+b, file=sys.stderr)
    #print(ans)
    assert(len(ans) == r + y + b)
    if ans[0] == ans[-1]:
        return 'IMPOSSIBLE'
    else:
        return ''.join(mapping[x] for x in ans)

if __name__ == '__main__':
    for t, l in enumerate(sys.stdin.readlines()[1:]):
        u = [int(x) for x in l.split()]
        print('Case #{}: {}'.format(t+1, solve(*u[1:])))
