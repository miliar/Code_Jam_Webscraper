def solve(test):
    print('Case #{}: '.format(test), end ="")

    n, k = map(int, input().split())

    places = [[n, 1]]
    while k > 0:
        nplace = []
        for l, num in places:
            if num >= k:
                print('%d %d' % ((l // 2, (l - 1) // 2)))
                return
            k -= num
            nplace.append((l // 2, num))
            nplace.append(((l - 1) // 2, num))
        nplace = sorted(nplace)[::-1]
        places = []
        for l, num in nplace:
            if len(places) > 0 and places[-1][0] == l:
                places[-1][1] += num
            else:
                places.append([l, num])
    print('0 0')
                


t = int(input())
for i in range(t):
    solve(i + 1)

