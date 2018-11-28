t = int(input())
for i in range(1, t + 1):
    s, f = [s for s in input().split(" ")]
    s = list(s)
    f = int(f)
    n = len(s)
    possible = True
    num_flip = 0
    for j in range(n):
        if j + f - 1 >= n:
            for k in range(j,n):
                if s[k] == '-':
                    possible = False
                    break
            if not possible:
                break
        else:
            if s[j] == '-':
                for k in range(j,j+f):
                    if s[k] == '-':
                        s[k] = '+'
                    else:
                        s[k] = '-'
                num_flip += 1

    ans = str(num_flip)
    if not possible:
        ans = "IMPOSSIBLE"
    print("Case #{}: {}".format(i, ans))

