

t = int(raw_input())

def solve(s, k):
    cnt = 0
    i = 0
    while i <= len(s) - k:
        if (s[i] != "-"):
            i += 1
        else:
            for j in xrange(i, i + k):
                if (s[j] == "-"):
                    s[j] = "+"
                else:
                    s[j] = "-"

            cnt += 1
            i += 1

    if "-" in s:
        return "IMPOSSIBLE"
    else:
        return cnt


for l in xrange(t):
    s, k = raw_input().split()
    k = int(k)
    s = list(s)

    print "Case #" + str(l + 1) + ": " + str(solve(s, k))
