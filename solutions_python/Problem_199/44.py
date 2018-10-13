t = int(input())

for task in range(t):
    s, k = input().split()
    k = int(k)
    s = [x == "+" for x in s]
    def flip(p):
        if p + k > len(s):
            return False
        for i in range(p, p + k):
            s[i] = not s[i]
        return True
    n = 0
    for i, x in enumerate(s):
        if not x:
            if flip(i):
                n += 1
            else:
                print("Case #{}: IMPOSSIBLE".format(task + 1))
                break
    else:
        print("Case #{}: {}".format(task + 1, n))
