def sign(x):
    return (x > 0) - (x < 0)

def multiply(a, b):
    return sign(a*b) * lookup[abs(a)-1][abs(b)-1]
    
def resolve(s):
    result = 1
    for c in s:
        result = multiply(result, ord(c)-103)
    return result
    
lookup = [[1, 2, 3, 4], [2, -1, 4, -3], [3, -4, -1, 2], [4, 3, -2, -1]]
         # 1, i, j, k

for tc in range(1, int(raw_input())+1):
    l, x = map(int, raw_input().split())
    s = raw_input()*x
    
    if resolve(s) != -1:
        print 'Case #%d: NO' % tc
        continue
    
    i = 0
    state = 0
    product = 1
    itoj = -1
    jtok = -1
    while True:
        product = multiply(product, ord(s[i])-103)
        if state == 0 and product == 2 and i > itoj:
            itoj = i
            state += 1
            product = 1
        elif state == 1 and product == 3 and i > jtok:
            jtok = i
            state += 1
            product = 1
            
        if i < l*x-1:
            i += 1
        else:
            if state == 0:
                print 'Case #%d: NO' % tc
                break
            elif state == 1:
                state = 0
                product = 1
                i = itoj
            elif state == 2 and product == 4:
                print 'Case #%d: YES' % tc
                break
            else:
                state = 1
                product = 1
                i = jtok
    
    