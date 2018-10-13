def flip(w):
    if w == "+":
        return  "-"
    else:
        return  "+"

def check(raw, num):
    size = len(raw)
    ans = 0
    for i in range(size - num + 1):
        if raw[i] == "-":
            raw[i] = "+"
            ans += 1
            for j in range(i + 1, i + num):
                raw[j] = flip(raw[j])
    for i in range(size - num + 1, size):
        if raw[i] == "-":
            ans = -1
    return ans

t = int(input())
s = [input().split() for i in range(t)]

for i in range(t):
    temp = check(list(s[i][0]), int(s[i][1]))
    if temp == -1:
        print("Case #{0}: IMPOSSIBLE".format(i + 1))
    else:
        print("Case #{0}: {1}".format(i + 1, temp))

