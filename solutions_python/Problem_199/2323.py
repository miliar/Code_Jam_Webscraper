def flip(s, k, start):
    for i in range(start, start + k):
        s[i] = not s[i]


def solve(s, k):
    count = 0
    for index in range(len(s) - 1, k - 2, -1):
        if not s[index]:
            flip(s, k, index - k + 1)
            count += 1
    return count if False not in s else "IMPOSSIBLE"


t = int(input())
for t_count in range(1, t + 1):
    s, k = tuple(input().split(" "))
    s = [True if x == "+" else False for x in s]
    k = int(k)
    print("Case #{0}: {1}".format(t_count, solve(s, k)))
