stdin = open('C-small-attempt0.in')
stdout = open('output.txt', 'w')

num = {
'11':'1', '1i':'i', '1j':'j', '1k':'k',
'i1':'i', 'ii':'-1', 'ij':'k', 'ik':'-j',
'j1':'j', 'ji':'-k', 'jj':'-1', 'jk':'i',
'k1':'k', 'ki':'j', 'kj':'-i', 'kk':'-1'
}
values = [
'1', '-1'
'i', '-i'
'j', '-j'
'k', '-k'
]

def prod(x, y):
    sig = 1
    if x[0] == '-':
        x = x[1:]
        sig *= -1
    if y[0] == '-':
        y = y[1:]
        sig *= -1
    z = num[x+y]
    if z[0] == '-':
        z = z[1:]
        sig *= -1
    if sig == -1:
        z = '-' + z
    return z


T = int( stdin.readline() )
for no in range(1, T+1):
    L,X = map(int, stdin.readline().split() )
    inp = stdin.readline().strip()
    inp = inp * X
    states = {(0,'1')}
    for i in inp:
        s1 = set((x,prod(y,i)) for x,y in states)
        s2 = set((1,'1') for x,y in s1 if x==0 and y=='i')
        s3 = set((2,'1') for x,y in s1 if x==1 and y=='j')
        states = s1 | s2 | s3
    if (2,'k') in states:
        ret = 'YES'
    else:
        ret = 'NO'
    print >>stdout, 'Case #{}: {}'.format(no, ret)
    
    
