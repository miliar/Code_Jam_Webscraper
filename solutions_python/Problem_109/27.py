import sys

sys.setrecursionlimit(5000)

def dfs(people, start_id, ans, L, W, start_I, start_J, origin_L, origin_W): # return end id
    if start_id == len(people):
        return start_id
    if L < 0 or W < 0:
        return start_id

    first = people[start_id]

    r = first[0]
    #if min(L, W) < r:
    #    return start_id


    pos_i = -1
    pos_j = -1
    if start_I == 0 and start_I + L == origin_L:
        pos_i = 0
    elif start_I == 0 and L >= r:
        pos_i = 0
    elif start_I + L == origin_L and L >= r:
        pos_i = start_I + r
    elif L >= 2*r:
        pos_i = start_I + r

    if start_J == 0 and start_J + W == origin_W:
        pos_j = 0
    elif start_J == 0 and W >= r:
        pos_j = 0
    elif start_J + W == origin_W and W >= r:
        pos_j = start_J + r
    elif W >= 2*r:
        pos_j = start_J + r

    if pos_i == -1 or pos_j == -1:
        return start_id
    
    ans[first[1]] = (pos_i, pos_j)
    start_id += 1
    end_i = pos_i + r
    end_j = pos_j + r
    wasted_L = end_i - start_I
    wasted_W = end_j - start_J
    if L > W:
        start_id = dfs(people, start_id, ans, wasted_L, W - wasted_W, start_I, end_j, origin_L, origin_W)
        start_id = dfs(people, start_id, ans, L-wasted_L, W, end_i, start_J, origin_L, origin_W)
    else: # W >= L
        start_id = dfs(people, start_id, ans, L-wasted_L, wasted_W, end_i, start_J, origin_L, origin_W)
        start_id = dfs(people, start_id, ans, L, W-wasted_W, start_I, end_j, origin_L, origin_W)
    return start_id


T = input()

for t in range(T):
    ans = {}
    N, W, L = map(int, raw_input().split())
    Rs = map(int, raw_input().split())

    people = list(reversed(sorted([(Rs[i], i) for i in range(N)])))

    dfs(people, 0, ans, L, W, 0, 0, L, W)

    print 'Case #%d:' % (t+1),
    for i in range(N):
        print ans[i][1], ans[i][0], 
    print ''

