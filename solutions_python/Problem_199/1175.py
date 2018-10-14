tc = int(input())
for t in range(tc):
    s, k = input().split()
    s = [int(i != '+') for i in s]
    k = int(k)
    r = 0
    for i in range(len(s) - k + 1):
        if s[i] == 1:
            r += 1
            for j in range(k):
                s[i + j] ^= 1
    if 1 in s:
        print("Case #{}: IMPOSSIBLE".format(t + 1))
    else:
        print("Case #{}: {}".format(t + 1, r))
