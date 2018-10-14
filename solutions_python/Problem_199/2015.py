def ans(x, s, k):
    print("Case #{}: {}".format(x, flips(s, k)))


def flips(s, k):
    s = list(s)
    c = 0
    for i in range(len(s)-k):
        if s[i] == "-":
            j = 0
            while j < k:
                if s[i+j] == "+":
                    s[i+j] = "-"
                else:
                    s[i+j] = "+"
                j += 1
            c += 1
    x = 0
    if s[len(s)-k] == "-":
        for i in range(len(s)-k, len(s)):
            if s[i] == "-":
                x += 1
        if x == k:
            c += 1
        else:
            return "IMPOSSIBLE"
    else:
        for i in range(len(s)-k, len(s)):
            if s[i] == "+":
                x += 1
        if x != k:
            return "IMPOSSIBLE"
    return c



for x in range (1, int(input())+1):
    s, k = input().split()
    k = int(k)
    ans(x, s, k)
