from itertools import count

def bla (c,f,x):
    best = x/2
    last = c/2
    for i in count(1):
        new = last+x/(2+f*i)
        if best > new:
            best = new
        else:
            break
        last += c/(2+f*i)
    return best

f = map(str.strip,open('B-large.in'))

case = 1
i = 1
while i < len(f):
    a = map(float,f[i].split())
    i += 1
    print 'Case #%d: %.7f'%(case, bla(*a))
    case += 1
