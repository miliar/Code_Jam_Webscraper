t = int(input())

for i in range(t):
    a = 0

    s, k = input().split()
    s = list(s)
    k = int(k)

    c = 0
    l = len(s)
    while c < l:
        if s[c] == '-':
            if c + k <= l:
                for cc in range(k):
                    if s[c + cc] == '-':
                        s[c + cc] = '+'
                    else:
                        s[c + cc] = '-'
                a += 1
            else:
                a = "IMPOSSIBLE"
                break
        c += 1

    print("Case #{}: {}".format(i + 1, a))
