def flip(s, i, k):
    a = map(lambda x: 1 if x == '+' else 0, s)
    for j in range(i, i+k):
        a[j] ^= 1
    return reduce(lambda x, y: x+'+' if y else x+'-', a, '')

def bfs(S, k):
    f = set([S])
    l = [(S,0)]
    h = 0
    n = len(S)
    while h != len(l):
        # print l[h:]
        s, p = l[h]
        if s == '+'*n:
            return p
        h += 1
        for i in range(n-k+1):
            ss = flip(s, i, k)
            if ss not in f:
                f.add(ss)
                l.append((ss, p+1))
    return 'IMPOSSIBLE'

def solv(s, k):
    js = 0
    for i in range(len(s)):
        c = s[i]
        if c == '-':
            if i+k <= len(s):
                s = flip(s, i, k)
                js += 1
            else:
                return "IMPOSSIBLE"
    return js

def main():
    n = int(raw_input())
    for i in range(n):
        s, k = raw_input().split(' ')
        ans = str(solv(s, int(k)))
        print "Case #%d: %s" %(i+1, ans)

if __name__ == "__main__":
    main()