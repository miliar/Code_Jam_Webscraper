def ispossible(c, r, m):
    if c==1 or r==1:
        return True
    if c==2 or r==2:
        if m == c*r - 2 or (m%2 != 0 and m != c*r - 1):
            return False
        return True
    if c*r - m in [2, 3, 5, 7]:
        return False
    return True

#grid in strlist form, w >= h (-> rotate back)
def getgridlist(c, r, m):
    w = max(c, r)
    h = min(c, r)
    if h == 1:
        return ['*'*m + '.'*(w-m-1) + 'c']
    elif h == 2:
        if m % 2 == 0:
            l1 = '*'*(m//2) + '.'*(w-m//2)
            l2 = l1[:-1] + 'c'
        else:
            l1 = '*'*w
            l2 = '*'*(w-1) + 'c'
        return [l1, l2]
    elif h == 3:
        if m == c*r-1:
            sol = ['*'*w, '*'*w, '*'*(w-1)+'c']
        else:
            sol = []
            sol.append('*'*(m//3) + '.'*(w-m//3-1) + 'c')
            sol.append('*'*(m//3) + '.'*(w-m//3))
            sol.append('*'*(m - 2*(m//3)) + '.'*(w - (m - 2*(m//3))))
        return sol
    elif h == 4:
        if m == c*r-1:
            sol = ['*'*w, '*'*w, '*'*w, '*'*(w-1)+'c']
        elif m == c*r-4:
            sol = ['*'*w, '*'*w, '*'*(w-2)+'.'*2, '*'*(w-2)+'.c']
        else:
            sol = []
            sol.append('*'*(m//4) + '.'*(w-m//4-1) + 'c')
            sol.append('*'*(m//4) + '.'*(w-m//4))
            last = m - (3*(m//4))
            if last == w-1:
                sol.append('*'*(m//4+1) + '.'*(w-m//4-1))
                last -= 1
            else:
                sol.append(sol[1])
            sol.append('*'*last + '.'*(w-last))
        return sol
    else:
        sols = [['.....', '.....', '.....', '.....', '....c'], ['*....', '.....', '.....', '.....', '....c'], ['**...', '.....', '.....', '.....', '....c'], ['***..', '.....', '.....', '.....', '....c'], ['**...', '**...', '.....', '.....', '....c']]
        sols += [['*****', '.....', '.....', '.....', '....c'], ['*****', '*....', '.....', '.....', '....c'], ['*****', '**...', '.....', '.....', '....c'], ['*****', '***..', '.....', '.....', '....c'], ['*****', '*....', '*....', '*....', '*...c']]
        sols += [['*****', '*****', '.....', '.....', '....c'], ['*****', '*****', '*....', '.....', '....c'], ['*****', '*****', '**...', '.....', '....c'], ['*****', '*****', '***..', '.....', '....c'], ['*****', '*****', '**...', '*....', '*...c']]
        sols += [['*****', '*****', '*****', '.....', '....c'], ['*****', '*****', '**...', '**...', '**..c'], ['*****', '*****', '***..', '**...', '**..c'], [], ['*****', '*****', '***..', '***..', '***.c']]
        sols += [[], ['*****', '*****', '*****', '***..', '***.c'], [], [], ['*****', '*****', '*****', '*****', '****c']]
        return sols[m]

def printgrid(c, r, m):
    l = getgridlist(c, r, m)
    if c < r:
        for x in range(0, r):
            for y in range(0, c):
                print(l[y][x], end='')
            print()
    else:
        for i in l:
            print(i)

t = int(input())
for tc in range(1, t+1):
    (r, c, m) = [int(x) for x in input().split()]
    print('Case #%i:' % (tc))
    if not ispossible(c, r, m):
        print('Impossible')
    else:
        printgrid(c, r, m)
