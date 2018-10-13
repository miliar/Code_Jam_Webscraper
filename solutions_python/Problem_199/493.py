import sys

sys.setrecursionlimit(30000)

def solve(s, k):
    c = s[0]
    i = 0
    while c == "+":
        i += 1
        if i == len(s):
            break
        c = s[i]
    
    if i == len(s):
        return 0
    
    if i > len(s) - k:
        return -1
    
    
    for j in range(i, i+k):
        if s[j] == "+":
            s = s[:j] + "-" + s[j+1:]
        else:
            s = s[:j] + "+" + s[j+1:]
    ans = solve(s[i+1:], k)
    if ans == -1 :
        return ans
    else:
        return ans+1

f = open("input1.in")
n = int(f.readline())
for m in range(n):
    l = f.readline().strip().split()
    s = l[0]
    k = int(l[1])
    ans = solve(s, k)
    if ans == -1:
        print("Case #%d: IMPOSSIBLE" % (m+1))
    else:
        print("Case #%d: %d" % (m+1, ans))

