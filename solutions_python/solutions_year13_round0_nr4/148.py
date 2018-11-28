import sys
from copy import copy

solved = {}

def get_chests_footprint(chests):
    res = []
    for c in chests:
        res.append(c['num'])
    res.sort()
    return tuple(res)

def solve(keys, chests):
    keys.sort()
    tk = tuple(keys)
    tc = get_chests_footprint(chests)
    #print (tk, tc)
    #print solved
    if (tk, tc) in solved:
        #print (tk, tc)
        return solved[(tk, tc)]
    for chest in chests:
        if chest['key'] in keys:
            _keys = copy(keys)
            _chests = copy(chests)
            _keys.remove(chest['key'])
            _chests.remove(chest)
            _keys.extend(chest['loot'])
            if len(_chests) == 0:
                solved[(tk, tc)] = str(chest['num'])
                return str(chest['num'])
            if len(_keys) == 0:
                continue
            res = solve(_keys, _chests)
            if res != 'IMPOSSIBLE':
                solved[(tk, tc)] = str(chest['num']) + ' ' + res
                return str(chest['num']) + ' ' + res
    solved[(tk, tc)] = 'IMPOSSIBLE'
    return 'IMPOSSIBLE'

with open(sys.argv[1]) as f:
    T = int(f.readline())
    for case in range(1,T+1):
        solved = {}
        (k, N) = map(int, f.readline().split(' '))
        keys = map(int, f.readline().split(' '))
        chests = []
        for n in xrange(0, N):
            line = map(int, f.readline().split(' '))
            chests.append({'num': n+1, 'key': line[0], 'loot': line[2:]})
        print 'Case #%i: %s' % (case, solve(keys, chests))
