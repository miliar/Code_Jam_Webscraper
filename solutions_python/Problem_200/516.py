def tidy(k):
    s = str(k)
    for j in range(1, len(s)):
        if s[j-1] > s[j]:
            return False
    return True

def solve(k):
    s = str(k)
    for j in range(1, len(s)):
        if s[j-1] > s[j]:   # Problem at s[j]
            n1 = int(s[:j]) - 1
            s1 = ''
            for i in range(j, len(s)):
                s1 += '9'
            s2 = str(n1)
            if s2 == "0":
                s2 = ''
            s = s2 + s1
            return solve(s)
    return s
            
f = open("input1.in")
n = int(f.readline())
for m in range(n):
    NN = int(f.readline().strip())
    print("Case #%d: %s" % (m+1, solve(NN)))

