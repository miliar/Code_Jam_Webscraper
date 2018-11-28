def check(s):
    confl = {'R': ('R','O','V'), 'O': ('O','R','Y'), 'Y': ('Y','O','G'), 'G': ('G','B','Y'), 'B': ('B','V','G'), 'V': ('V','R','B')}
    for i in range(len(s)):
        if s[(i+1)%len(s)] in confl[s[i]]:
            assert False

def solve():
    n,r,o,y,g,b,v = map(int, input().split())
    
    sbo = ''
    nbo = o
    sbo += 'BO'*nbo
    b -= nbo
    o -= nbo
    if b < 0:
        print('IMPOSSIBLE')
        return
    if r+o+y+g+b+v > 0 and nbo > 0:
        sbo += 'B'
        b -= 1
    if b < 0:
        print('IMPOSSIBLE')
        return
    
    srg = ''
    nrg = g
    srg += 'RG'*nrg
    r -= nrg
    g -= nrg
    if r < 0:
        print('IMPOSSIBLE')
        return
    if r+o+y+g+b+v > 0 and nrg > 0:
        srg += 'R'
        r -= 1
    if r < 0:
        print('IMPOSSIBLE')
        return
    
    syv = ''
    nyv = v
    syv += 'YV'*nyv
    y -= nyv
    v -= nyv
    if y < 0:
        print('IMPOSSIBLE')
        return
    if r+o+y+g+b+v > 0 and nyv > 0:
        syv += 'Y'
        y -= 1
    if y < 0:
        print('IMPOSSIBLE')
        return
    
    if r+o+y+g+b+v == 0:
        res = sbo + srg + syv
        print(res)
        check(res)
        return
    
    #r,y,b
    #num = {'R': r, 'Y': y, 'B': b}
    order = sorted([[r,'R'],[y,'Y'],[b,'B']])
    #print('DEBo', order)
    s1 = (order[1][1] + order[2][1]) * order[1][0] # 121212...12
    order[2][0] -= order[1][0]
    order[1][0] = 0
    n2 = min(order[0][0], order[2][0])
    s2 = (order[0][1] + order[2][1]) * n2 # 0202...02
    order[0][0] -= n2
    order[2][0] -= n2
    # could still have 0s or 2s
    if order[0][0] > 0:
        s1pr = [x+y for x,y in zip(s1,order[0][1]*order[0][0])]
        s1 = ''.join(s1pr) + s1[order[0][0]:]
    elif order[2][0] > 0:
        # can still put a 2
        # - in front of s1 if there are also mixed strings
        # - between the mixed strings using 1 and using 0, if they exist
        #-> only one place, different depending on order, all equiv
        if order[2][0] > 1 or nbo+nyv+nrg == 0:
            print('IMPOSSIBLE')
            return
        s1 = order[2][1] + s1
        order[2][0] -= 1
        
    #order in the end: 1m1m1 + 2m2m2 + 0m0m0 + 1(0)2(0)1212 + 020202
    #                                              s1           s2
    if order[0][1] == 'R':
        m0 = srg
    elif order[1][1] == 'R':
        m1 = srg
    else: #order[2][1] == 'R':
        m2 = srg
    if order[0][1] == 'Y':
        m0 = syv
    elif order[1][1] == 'Y':
        m1 = syv
    else: #order[2][1] == 'Y':
        m2 = syv
    if order[0][1] == 'B':
        m0 = sbo
    elif order[1][1] == 'B':
        m1 = sbo
    else: #order[2][1] == 'B':
        m2 = sbo
    
    #print('DEBs', m1,',',m2,',',m0,',',s1,',',s2)
    res = m1 + m2 + m0 + s1 + s2
    print(res)
    check(res)


if __name__ == '__main__':
    t = int(input())
    for tc in range(1,t+1):
        print("Case #{}: ".format(tc), end='')
        solve()
        #print('')
