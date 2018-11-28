from itertools import \
    product, \
    permutations, \
    combinations, \
    combinations_with_replacement
from functools import reduce, lru_cache
from math import floor,ceil,inf,sqrt
import operator
colors = {'R':('R'),
          'Y':('Y'),
          'B':('B'),
          'O':('R','Y'),
          'G':('Y','B'),
          'V':('R','B')}

order = ['R', 'O', 'Y', 'G', 'B', 'V']

from itertools import \
    product, \
    permutations, \
    combinations, \
    combinations_with_replacement
from functools import reduce, lru_cache
from math import floor,ceil,inf,sqrt

order = ['R', 'O', 'Y', 'G', 'B', 'V']

def solve(colors):
    assert(colors['O'] == colors['V'] == colors['G'] == 0)

    x = sorted(colors.items(), key=lambda x: -x[1])[0][0]
    y = sorted(colors.items(), key=lambda x: -x[1])[1][0]
    z = sorted(colors.items(), key=lambda x: -x[1])[2][0]

    overlap = colors[y]+colors[z]-colors[x]
    if overlap < 0:
        return 'IMPOSSIBLE'
    
    ans = []
    for i in range(colors[x]):
        ans += x
        if overlap > 0:
            ans += y
            colors[y] -= 1
            ans += z
            colors[z] -= 1
            overlap -= 1
        elif colors[y] > 0:
            ans += y
            colors[y] -= 1
        elif colors[z] > 0:
            ans += z
            colors[z] -= 1

    return ''.join(ans)            
        
if __name__ == '__main__':
    import sys,re
    data = iter(sys.stdin.read().splitlines())
    T = int(next(data))
    for (case_num, case) in enumerate(data):
        colors = {order[x[0]-1]:int(x[1])
                  for x in enumerate(case.split())}
        print('Case #{}: {}'.format(case_num+1, solve(colors)))
