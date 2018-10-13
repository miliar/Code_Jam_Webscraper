# lizesheng
#


def solve(s, k):
    length = len(s)
    s = [1 if c=='+' else 0 for c in s]
    k = int(k)
    NOPE = "IMPOSSIBLE"

    count = 0
    for i, c in enumerate(s):
        if (length-i) < k:
            if not c:
                return NOPE
            else:
                continue

        if c == 0:
            for j in range(i, i+k):
                s[j] ^=1
            count +=1
    return count


t = int(input())
for i in range(1, t + 1):
    s, k = [x for x in input().split(" ")]
    print("Case #{}: {}".format(i, solve(s, k)))
