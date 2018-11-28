import heapq
def print_answer(casenum, ans):
    print('Case #{0}: {1} {2}'.format(casenum, *ans))

def solve(N, K):
    pass

def _simulation(N, K):
    rooms = [True for i in range(N)]
    for _ in range(K):
        ls = []
        space = 0
        for i in range(N):
            ls.append(space)
            if rooms[i]:
                space += 1
            else:
                space = 0
        rs = []
        space = 0
        for i in range(N-1, -1, -1):
            rs.append(space)
            if rooms[i]:
                space += 1
            else:
                space = 0
        rs.reverse()
        # print(ls)
        # print(rs)
        max_min_lr_idx = 0
        max_min_lr = 0
        max_max_lr_idx = 0
        max_max_lr = 0
        for i in range(N):
            if not rooms[i]:
                continue
            if max_min_lr < min(ls[i], rs[i]):
                max_min_lr = min(ls[i], rs[i])
                max_min_lr_idx = i
                max_max_lr = max(ls[i], rs[i])
                max_max_lr_idx = i
            if max_min_lr == min(ls[i], rs[i]) and max_max_lr < max(ls[i], rs[i]):
                max_max_lr = max(ls[i], rs[i])
                max_max_lr_idx = i
        rooms[max_max_lr_idx] = False
        # print('X' + ''.join(['.' if x else 'X' for x in rooms]) + 'X')
    return max_max_lr, max_min_lr

def simulation(N, K):
    rooms = []
    rooms.append(-N)
    for _ in range(K):
        v = heapq.heappop(rooms)
        v = -v - 1
        if v == 0:
            ma = mi = 0
            continue
        if v%2 == 0:
            ma = mi = v//2
        else:
            ma = v//2 + 1
            mi = v//2
        if ma > 0:
            heapq.heappush(rooms, -ma)
        if mi > 0:
            heapq.heappush(rooms, -mi)
    return ma, mi

def main():
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        ans = simulation(N, K)
        print_answer(i+1, ans)

def test():
    for N in range(1, 51):
        for K in range(1, N+1):
            ans = simulation(N, K)
            _ans= _simulation(N, K)
            if ans != _ans:
                print(N, K, ans, _ans)


if __name__ == '__main__':
    main()
    # test()