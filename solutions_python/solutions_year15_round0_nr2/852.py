f = open('./pyoutput2.txt', 'w')

for t in range(int(input())):

    D = int(input())

    P = list(map(int, input().split()))

    # 结果显然至多不会超过 max(P)，也就是完全不分配的情况
    ans = max(P)

    # 遍历分配块的大小，然后最优化时间
    Z = 2
    while Z < ans:
        ans = min(ans, sum([(x - 1) // Z for x in P]) + Z)
        Z += 1
    f.write('Case #%d: %s\n' % (t + 1, ans))
    print('Case #%d: %s' % (t + 1, ans))
f.close()