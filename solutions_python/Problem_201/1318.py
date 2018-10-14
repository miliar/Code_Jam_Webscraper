

def solve_all(n, k):
    cur_segs = [(n, 1)]

    for i in range(1, n + 1):
        cur_segs.sort(key=lambda x: (-x[0], x[1]))
        #print(cur_segs)
        stall = cur_segs[0]
        cur_segs = cur_segs[1:]
        
        sz, start = stall
        #print('Person chooses stall inside ', start, start + sz - 1)
        split_place = None
        if sz & 1:
            split_place = start + sz // 2
        else:
            split_place = start + sz // 2 - 1
        #print('  place', split_place)

        end = start + sz - 1
        if split_place != start:
            cur_segs.append((split_place - start, start))
        if split_place != end:
            cur_segs.append((end - split_place, split_place + 1))

        if i == k:
            if sz & 1:
                return (sz // 2, sz // 2)
            else:
                return (sz // 2, sz // 2 - 1)

def solve():
    n, k = map(int, input().split())
    res = solve_all(n, k)
    return ' '.join(map(str, res))

t = int(input())
for i in range(1, t + 1):
    print('Case #{}: {}'.format(i, solve()))
