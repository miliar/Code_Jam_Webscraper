import sys

def analyze(s):
    ans = []
    count = 1
    prev = s[0]
    for c in s[1:]:
        if c != prev:
            ans.append((prev, count))
            prev = c
            count = 1
        else:
            count += 1
    ans.append((prev, count))
    return ans

def diff(t1, t2):
    ans = 0
    for i in range(len(t1)):
        ans += abs(t1[i][1] - t2[i][1])
    return ans

def solve(s1, s2):
    t1 = analyze(s1)
    t2 = analyze(s2)
    c1 = [e[0] for e in t1]
    c2 = [e[0] for e in t2]
    if c1 != c2:
        return "Fegla Won"
    else:
        return str(diff(t1, t2))

T = int(sys.stdin.readline())
for i in range(1, T+1):
    dummy = sys.stdin.readline()
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
#    print analyze(s1), analyze(s2)
    print "Case #{0}: {1}".format(i, solve(s1, s2))

