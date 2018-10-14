from math import pi as PI
fin = open("a.in", 'r')
fout = open("a.out", 'w')


def count(i, k):
    ans = 0
    #print(i, end=' ')
    while (i != 0):
        ans += (i % 2)
        i //= 2
    #print(ans, k, ans==k)
    return (ans == k)


def calc(i, pc):
    ans = 0
    maxr = 0
    n = len(pc)
    for _ in range(n):
        if (i % 2 == 1):
            ans += 2 * PI * pc[_][0] * pc[_][1]
            maxr = max(maxr, pc[_][0])
        i //= 2
    return ans + PI * (maxr ** 2) 


def solve(num):
    n, k = map(int, fin.readline().split())
    pc = []
    for i in range(n):
        pc.append(list(map(int, fin.readline().split())))
    ans = 0
    for i in range(1 << n):
        if (count(i, k)):
            ans = max(ans, calc(i, pc))
    print("Case #{}: {}".format(num, ans))
    print("Case #{}: {}".format(num, ans), file=fout)


n = int(fin.readline())
for i in range(1, n + 1):
    solve(i)
fin.close()
fout.close()