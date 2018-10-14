f = open('C-small.in')
g = open('small.out', 'w')

T = int(f.readline()[:-1])

d = {('i', 'j'): 'k',
     ('j', 'i'): '-k',
     ('i', 'k'): '-j',
     ('k', 'i'): 'j',
     ('j', 'k'): 'i',
     ('k', 'j'): '-i'}

def mul(x, y) :
    if len(x) * len(y) == 4 : return mul(x[-1], y[-1])
    if len(x) * len(y) == 2 :
        res = mul(x[-1], y[-1])
        if len(res) == 1 : return '-' + res
        return res[1]
    if x == '1' : return y
    if y == '1' : return x
    if x == y : return '-1'
    return d[x, y]

def mulS(s) :
    res = s[0]
    for i in range(1, len(s)) : res = mul(res, s[i])
    return res

def solve(s) :
    if mulS(s) != '-1' : return 'NO'
    target = 'i'
    res = s[0]
    for i in range(1, len(s)) :
        if res == target :
            if target == 'i' :
                target = 'j'
                res = '1'
            else : return 'YES'
        res = mul(res, s[i])
    return 'NO'

for case in range(T) :
    L, X = map(int, f.readline()[:-1].split())
    L = f.readline()[:-1]
    res = solve(L*X)
    output = 'Case #' + str(case+1) + ': ' + str(res)
    print output
    g.write(output + '\n')

f.close()
g.close()
