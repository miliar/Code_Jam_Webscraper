def flip(s, start, k):
    arr = list(s)
    for i in range(start, start + k):
        if arr[i] == '-':
            arr[i] = '+'
        else:
            arr[i] = '-'
    return ''.join(arr)

def solve(s, k):
    ans = 0
    i = 0
    while i < len(s) - k + 1:
        if s[i] == '-':
            s = flip(s, i, k)
            ans += 1
        else:
            i += 1
    if s != '+'*len(s):
        return "IMPOSSIBLE"
    else:
        return str(ans)

t = int(raw_input())
for q in range(t):
    s, k = raw_input().split()
    k = int(k)
    print "Case #%d: %s" % (q + 1, solve(s, k))
