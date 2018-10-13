def solve(s, k):
    res = 0
    p = 0
    while len(s) != p:
        if s[p] == '-':
            if len(s) - p < k:
                return -1
            for i in range(k):
                c = '!'
                if s[p + i] == '-':
                    c = '+'
                else:
                    c = '-'
                s[p + i] = c
            res += 1
        else:
            s = s[1:]
        ++p

    return res

test_cnt = int(input())

for test in range(1, test_cnt + 1):
    s, k = [sub for sub in input().split(" ")]
    k = int(k)
    res = solve(list(s), k)

    if res == -1:
        res = "IMPOSSIBLE"
    else:
        res = str(res)
    print("Case #" + str(test) + ": " + res)
