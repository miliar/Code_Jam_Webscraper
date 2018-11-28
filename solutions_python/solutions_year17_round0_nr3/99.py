import heapq
from collections import defaultdict

precomp = {}

# merge dicts
def solve(cash, x):
    if x in precomp:
        return precomp[x]
    if x in cash:
        return cash[x]
#    print x
    left = (x - 1) / 2
    right = x / 2
    sol_left = solve(cash, left)
    sol_right = solve(cash, right)
    merged = {(left,right): 1}
    for y in sol_left:
        merged[y] = sol_left[y]
    for y in sol_right:
        if y in merged:
            merged[y] += sol_right[y]
        else:
            merged[y] = sol_right[y]
    cash[x] = merged
    return merged

def get_last(n, k):
    cash = defaultdict(int)
    solved = solve(cash, n)
    mega_merge = defaultdict(int)
#    print big_merge
#    print solved
    for key in solved:
        mega_merge[key] += solved[key]
#        ll = precomp[key]
#        for pair in ll:
#            mega_merge[pair] += solved[key] * ll[pair]
    s_list = []
    for key in sorted(mega_merge.keys()):
        s_list.append((key, mega_merge[key]))
#    print s_list
    total = 0
    for key,t in reversed(s_list):
        total += t
        if total >= k:
            return '{} {}'.format(max(key), min(key))
    print total, k

def precompute():
    for i in reversed(range(0, 1000)):
        item_list = []
        h = [(-i, 0)]
        for u in range(i):
            x = heapq.heappop(h)
            ret = split(h, x)
            if len(item_list) == 0:
                item_list.append([ret, 1])
            else:
                back = item_list[-1]
                back_tup = back[0]
                if back_tup == ret:
                    back[1] += 1
                else:
                    item_list.append([ret, 1])
#        print i, map(lambda x: x[1], item_list)
#        print i, item_list
        mappy = defaultdict(int)
        for x in item_list:
            val, count = x
            mappy[val] += count
#        print i, mappy
        precomp[i] = mappy

def split(h, interval):
#    print interval
    l, start = interval
    l = -l
    left = (l-1) / 2
    left_item = (-left, start) 
    right_item = (-(l - left - 1), left + 1)
#    print left_item, right_item
    heapq.heappush(h, left_item)
    heapq.heappush(h, right_item)
    return (left, l - left - 1)

precompute()
t = input()
for i in range(1, t+1):
    n, k = map(int, raw_input().strip().split())
    print 'Case #{}: {}'.format(i, get_last(n, k))
