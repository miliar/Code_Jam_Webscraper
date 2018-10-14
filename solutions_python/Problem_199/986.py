
def flip(x):
    c = ''
    for e in x:
        if e == '+':
            c+= '-'
        else:
            c+='+'
    return c

def pancake(s, k):
    if set(s) == {'+'}:
        return 0
    c = 0
    i = s.index('-')
    while i <= len(s) - k:
        temp = s[i:i+k]
        prev = s[:i]
        next = s[i+k:]
        s = prev + flip(temp) + next
        c += 1
        if set(s) == {'+'}:break
        i = s.index('-')
    if set(s) == {'+'}: return c
    return 'IMPOSSIBLE'



n = int(raw_input().strip())
for i in range(n):
    s, k = raw_input().strip().split()
    k = int(k)
    print 'Case #%d: %s' % (i+1, pancake(s, k))
