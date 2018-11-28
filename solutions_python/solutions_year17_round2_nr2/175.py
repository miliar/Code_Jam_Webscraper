def f(n, colors):
    r,o,y,g,b,v = colors

    if r == g and r + g == n:
        return 'RG'*r
    elif b == o and b + o == n:
        return 'BO'*b
    elif y == v and y + v == n:
        return 'YV'*y
    
    if (g > 0 and r <= g or
        o > 0 and b <= o or
        v > 0 and y <= v):
        return 'IMPOSSIBLE'

    comps = {}
    
    if g > 0:
        comps['R'] = 'RG'*g + 'R'
        r -= g

    if o > 0:
        comps['B'] = 'BO'*o + 'B'
        b -= o
    
    if v > 0:
        comps['Y'] = 'YV'*v + 'Y'
        y -= v

    if r > b + y or b > r + y or y > r + b:
        return 'IMPOSSIBLE'
        
    prims = sorted([('R', r), ('B', b), ('Y', y)], key = lambda x:x[1])
    
    str = ''

    triple = prims[0][1] + prims[1][1] - prims[2][1]
    assert triple >= 0

    for i in range(0, prims[2][1]):
        if prims[2][0] in comps:
            str += comps[prims[2][0]]
            del comps[prims[2][0]]
        else:
            str += prims[2][0]
        
        if i < prims[1][1]:
            if prims[1][0] in comps:
                str += comps[prims[1][0]]
                del comps[prims[1][0]]
            else:
                str += prims[1][0]

        if i >= prims[1][1] or i < triple:
            if prims[0][0] in comps:
                str += comps[prims[0][0]]
                del comps[prims[0][0]]
            else:
                str += prims[0][0]
            
    assert len(str) == n

    return str

def check(str):
    c = str[0]
    str += c

    for i in range(1, len(str)):
        c2 = str[i]

        if not (c == 'R' and (c2 == 'B' or c2 == 'Y' or c2 == 'O' or c2 == 'V') or
            c == 'B' and (c2 == 'Y' or c2 == 'R' or c2 == 'V' or c2 == 'G') or
            c == 'Y' and (c2 == 'R' or c2 == 'B' or c2 == 'G' or c2 == 'O') or
            c == 'G' and c2 == 'R' or
            c == 'O' and c2 == 'B' or
            c == 'V' and c2 == 'Y'):
            
            print("Incorrect", c, c2)
            return

        c = c2
        


t = int(input())
for testCase in range(t):
    colors = list(map(int, input().split()))
    n = colors.pop(0)
    
    ans = f(n, colors)

#    if ans != 'IMPOSSIBLE':
#        check(ans)

    print('Case #' + str(testCase+1) + ':', f(n, colors))
