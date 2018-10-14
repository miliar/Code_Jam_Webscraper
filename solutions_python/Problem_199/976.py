T = int(input())

def replace(s):
    r = ''
    for i in s:
        if i == '+':
            r += '-'
        else:
            r += '+'
    return r

for I in range(1, T+1):
    s, k = input().split()
    k = int(k)
    i = 0
    r = 0
    while i <= len(s) - k:
        if s[i] == '-':
            s = s[:i] + replace(s[i:i+k]) + s[i+k:]
            r += 1
        i += 1
    if s.count('-') > 0:
        print('Case #%s: IMPOSSIBLE' % I)
    else:
        print('Case #%s: %s' % (I, r))
