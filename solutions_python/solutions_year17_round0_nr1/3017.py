for t in range(int(input())):
    s, k = [item for item in input().split()]
    n = len(s)
    s = list(s)
    k = int(k)
    print("Case #{}: ".format(t + 1), end = "")
    ans = 0
    for i in range(n):
        if s[i] == "+":continue
        ans += 1
        for j in range(i, i + k):
            if j >= n:
                ans = -1
                break
            if s[j] == "+":
                s[j] = "-"
            else:
                s[j] = "+"
        else:
            continue
        break
    if ans == -1:
        print("IMPOSSIBLE")
    else:
        print(ans)