from multiprocessing import Pool

nt = int(raw_input())

istr = 'i'
jstr = 'j'
kstr = 'k'
ostr = '1'
nistr = '-i'
njstr = '-j'
nkstr = '-k'
nostr = '-1'

def isneg(a):
    return (a == nistr or
            a == njstr or
            a == nkstr or
            a == nostr)

def neg(a):
    if a == nistr: return istr
    if a == njstr: return jstr
    if a == nkstr: return kstr
    if a == nostr: return ostr
    if a == istr: return nistr
    if a == jstr: return njstr
    if a == kstr: return nkstr
    if a == ostr: return nostr

def mult(a, b):
    if a == ostr:
        return b
    if b == ostr:
        return a
    if a == b:
        return nostr
    if isneg(a) and isneg(b):
        return mult(neg(a), neg(b))
    if isneg(a):
        return neg(mult(neg(a), b))
    if isneg(b):
        return neg(mult(a, neg(b)))
    if a == istr and b == jstr:
        return kstr
    if a == jstr and b == kstr:
        return istr
    if a == kstr and b == istr:
        return jstr
    if a == jstr and b == istr:
        return nkstr
    if a == kstr and b == jstr:
        return nistr
    if a == istr and b == kstr:
        return njstr
    
    
def answer(t):
    l,x,s = t
    
    if l * x <= 2:
        return 'NO'
    
    s = ''.join([s for i in range(x)])
    l = l * x
    
    # arr[i][j] = value of string from i to (l-j)
    arr = [[None for j in range(l - i)] for i in range(l)]
    
    for i in range(l):
        prod = ostr
        for j in range(l-i-1, -1, -1):
            newprod = mult(prod, s[l-j-1])
            arr[i][j] = newprod
            prod = newprod
            
    for first_cutoff in range(2, l):
        if arr[0][first_cutoff] != 'i':
            continue
        for second_cutoff in range(1, first_cutoff):
            if arr[l-first_cutoff][second_cutoff] != 'j':
                continue
            if arr[l-second_cutoff][0] != 'k':
                continue
            return 'YES'
        
    return 'NO'

inputs = []

for i in range(nt):
    [l, x] = map(int, raw_input().split())
    s = raw_input()
    inputs.append((l,x,s))
    
p = Pool(4)
answers = p.map(answer, inputs)
    
for i, ans in enumerate(answers):
    print "Case #{}:".format(i+1),
    print ans
