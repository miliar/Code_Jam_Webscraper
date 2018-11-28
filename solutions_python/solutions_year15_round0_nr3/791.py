text = open('C-small-attempt0.in')
test_cases = int(text.readline())


def cross(m,n):
    if m=='1':
        if n=='1': return '1'
        elif n=='i': return 'i'
        elif n=='j': return 'j'
        elif n=='k': return 'k'
    elif m=='i':
        if n=='1': return 'i'
        elif n=='i': return '-1'
        elif n=='j': return 'k'
        elif n=='k': return '-j'
    elif m=='j':
        if n=='1': return 'j'
        elif n=='i': return '-k'
        elif n=='j': return '-1'
        elif n=='k': return 'i'
    else:
        if n=='1': return 'k'
        elif n=='i': return 'j'
        elif n=='j': return '-i'
        elif n=='k': return '-1'

def product(s):
    s = ','.join(s)
    p = s.split(',')
    t = '1'
    fin = ''
    for k in range(len(p)):
        res = cross(t[-1],p[k])
        if t[0]=='-':
            if res[0]=='-':
                t=res[1:]
            else:
                t=t[0]+res
        else:
            t=res
        if t=='i' and fin=='':
            fin='i'
            t='1'
        if t=='j' and fin=='i':
            fin='ij'
            t='1'
        if t=='k' and fin=='ij' and k==len(p)-1:
            fin='ijk'
            t='1'
    return t,fin

for i in range(test_cases):
    case = text.readline()
    l = case.split(' ')
    size = int(l[0])
    rep = int(l[1])
    test = text.readline()
    test = test.split('\n')
    string = test[0]*rep
    result,fin = product(string)
    if result=='1' and fin=='ijk':
        print('Case #'+str(i+1)+':','YES')
    else:
        print('Case #'+str(i+1)+':','NO')



    
    
