# coding: utf-8


M = [ # 1, i, j, k
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 4],  # 1
    [0, 2, -1, 4, -3],  # i
    [0, 3, -4, -1, 2],  # j
    [0, 4, 3, -2, -1],  # k
]


def mul(x, y):
    sign_x = -1 if x < 0 else 1
    sign_y = -1 if y < 0 else 1
    return M[abs(x)][abs(y)] * sign_x * sign_y


D = [[0 for i in range(5)] for j in range(5)]

for x in range(1, 5):
    for y in range(1, 5):
        z = M[x][y]
        if z > 0:
            D[z][x] = y
        else:
            D[-z][x] = -y


def div(x, y):
    sign_x = -1 if x < 0 else 1
    sign_y = -1 if y < 0 else 1
    return D[abs(x)][abs(y)] * sign_x * sign_y


def work():
    L, X = map(int, raw_input().split())
    s = raw_input()
    a = []
    for c in s:
        if c == 'i':
            a.append(2)
        elif c == 'j':
            a.append(3)
        elif c == 'k':
            a.append(4)

    if L == 1:
        return 'NO'

    n = L * X
    a = a * X
    s = [0 for i in range(n + 1)]
    s[0] = 1

    ci = []
    for i in range(1, n + 1):
        s[i] = mul(s[i - 1], a[i - 1])
        if s[i] == 2:
            ci.append(i)

    cj = []
    for j in range(2, n + 1):
        if div(s[n], s[j]) == 4:
            cj.append(j)

    for i in ci:
        for j in reversed(cj):
            if j <= i:
                break
            if div(s[j], s[i]) == 3:
                return 'YES'

    return 'NO'


def main():
    n_testcase = int(raw_input())
    for case in range(1, n_testcase + 1):
        ans = work()
        print 'Case #%s: %s' % (case, ans)


if __name__ == "__main__":
    main()
