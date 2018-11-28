def do():
    times = input()
    for i in xrange(times):
        print 'Case #%d:'%(i+1),
        calculate()

def repeat(string,n):
    for i in xrange(n):
        for char in string:
            yield char

def mul_quat(a,b):
    nega = False
    minus = '-'
    if a.startswith(minus):
        a = a.strip(minus)
        nega = not nega
    if b.startswith(minus):
        b = b.strip(minus)
        nega = not nega
    
    if a == b:
        return '1' if nega else '-1'
    if a == '1':
        return minus+b if nega else b
    if b == '1':
        return minus+a if nega else a

    L = list('ijk')
    L.remove(a)
    L.remove(b)
    if a+b in ('ij','jk','ki'):
        return minus+L[0] if nega else L[0]
    else:
        return L[0] if nega else minus+L[0]

def iter_chain(*argv):
    for i in argv:
        for _ in i:
            yield _

def calculate():
    n,r = map(int,raw_input().split())
    l = raw_input()
    
    value = total = '1'
    matches = ['i','j','k']
    
    if r%4 == 0:
        print "NO"
        return
    
    for char in repeat(l,1):
        total = mul_quat(total,char)
    
    total_ = total
    for i in xrange((r-1)%4):
        total_ = mul_quat(total_,total)
    
    if total_ != '-1':
        print "NO"
        return

    rb = 8
    
    for char in iter_chain(repeat(l,min(r,rb)),
                           repeat([total],(r-min(r,rb))%16)):
        value = mul_quat(value,char)
        if len(matches) > 1 and matches[0] == value:
            matches.pop(0)
            value = '1'

    if len(matches) == 1 and matches[0] == value:
        print "YES"
    else:
        print "NO"



if __name__ == '__main__':
    do()

