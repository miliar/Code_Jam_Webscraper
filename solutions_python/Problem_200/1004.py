import sys

def le(s1, s2):
    return ord(s1) <= ord(s2)

def solve(s):
    if s == 0:
        return ""
    maxIndex = len(s) - 1

    for i in range(maxIndex):
        if not le(s[i], s[i + 1]):
            return solve(str(int(s[:i+1]) - 1)) + ("9" * (maxIndex - i))

    return s


t = int(sys.stdin.readline().strip())
for i in range(t):
    num = sys.stdin.readline().strip()
    print("Case #%d: %d" % (i+1, int(solve(num))))
