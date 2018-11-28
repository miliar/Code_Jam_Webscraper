def flip(s, k):
    k = int(k)
    s = map(lambda x:0 if x=='-' else 1, list(s))
    ans = 0
    for i in range(len(s)-k+1):
        if s[i] == 0:
            s[i:i+k] = map(lambda x:x^1, s[i:i+k])
            ans += 1
    return ans if 0 not in s else 'IMPOSSIBLE'

f = open('output-1', 'wr')
N = int(raw_input())
for i in range(1, N+1):
    f.write('Case #%d: %s\n' % (i, flip(*raw_input().split())))
f.close()
