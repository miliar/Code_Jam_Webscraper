
d = {
    ('i','j'):('k',1),
    ('j','i'):('k',-1),
    ('i','k'):('j',-1),
    ('k','i'):('j',1),
    ('j','k'):('i',1),
    ('k','j'):('i',-1)
}

def dij(x,y):
    if x == '1':
        return y,1
    if y == '1':
        return x,1
    if x == y:
        return '1',-1
    return d[(x,y)]

for case in range(1,int(raw_input())+1):
    L,X = map(int,raw_input().split())
    s = raw_input()*X
    result = False
    if L*X >= 3 and len(set(s))>1:
        a = '1'
        sign = 1
        stack = [('i',1),('k',1)]
        for i in range(len(s)):
            a,newsign = dij(a,s[i])
            sign *= newsign
            if stack and stack[0] == (a,sign):
                stack.pop(0)
        if not stack and (a,sign) == ('1',-1):
            result = True

    print 'Case #%d: %s' %(case,'YES' if result else 'NO')



