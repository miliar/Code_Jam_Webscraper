import sys

def get_uniq (s):
    a = [s[0]]
    for i in range(len(s)):
        if s[i] != a[len(a)-1]:
            a.append(s[i])
    return ''.join(a)

def get_num (s):
    a = []
    eq  = s[0]
    cnt = 0
    for i in range(len(s)):
        if s[i] == eq:
            cnt += 1
        else:
            a.append(cnt)
            cnt = 1
            eq  = s[i]
    a.append(cnt)
    return a

def find_min(s):
    s = sorted(s)
    m = 10000000
    for a in range(s[0],s[-1]+1):
        c = 0
        for j in range(len(s)):
            c += abs(s[j] - a)
        m = min(c, m)
    return m

def solve(s):
    a = get_uniq(s[0])
    for i in range(len(s)):
        if get_uniq(s[i]) != a:
            return 'Fegla Won'
    num = []
    for i in range(len(s)):
        num.append(get_num(s[i]))
    res = 0
    for i in range(len(num[0])):
        sl = [num[x][i] for x in range(len(s))]
        res += find_min(sl)
    return str(res)

f = sys.stdin
T = int(f.readline().strip())
for i in range(1,T+1):
    N = int(f.readline().strip())
    s = []
    for a in range(N):
        s.append(f.readline().strip())
    r = solve(s)
    sys.stdout.write('Case #%d: %s\n' % (i, r))