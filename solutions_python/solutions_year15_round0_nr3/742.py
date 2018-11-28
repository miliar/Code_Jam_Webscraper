import sys

matr = {
    ('1', '1'): (1, '1'),  ('1', 'i'): (1, 'i'),  ('1', 'j'): (1, 'j'),  ('1', 'k'): (1, 'k'),
    ('i', '1'): (1, 'i'),  ('i', 'i'): (-1, '1'), ('i', 'j'): (1, 'k'),  ('i', 'k'): (-1, 'j'),
    ('j', '1'): (1, 'j'),  ('j', 'i'): (-1, 'k'), ('j', 'j'): (-1, '1'), ('j', 'k'): (1, 'i'),
    ('k', '1'): (1, 'k'),  ('k', 'i'): (1, 'j'),  ('k', 'j'): (-1, 'i'), ('k', 'k'): (-1, '1'),
}

def mult(a, b):
    z, v = matr[(a[1], b[1])]
    return (a[0]*b[0]*z, v)    

def next_line():
    line = sys.stdin.readline().strip("\n")
    #print line
    return line

def find_letter(ls, first, l):
    res = (1, '1')
    found = False
    for i in range(first, len(ls)):
        if res == l:
            found = True
            break
        res = mult(res, ls[i])
    return found, i

test_cases = int(next_line())

for tc in range(1, test_cases+1):
    L, X = [int(x) for x in next_line().split()]
    letters = [(1, x) for x in next_line()]
    product = (1, '1')
    for l in letters:
        product = mult(product, l)
    #print product
    if product[1] == '1':
        if product[0] == -1 and X % 2 == 1:
            req_cond = True
        else:
            req_cond = False
    else:
        if X % 2 == 0 and (X/2) % 2 == 1:
            req_cond = True
        else:
            req_cond = False

    result = 'NO'
    if req_cond:
        ls = letters * min(16, X)
        found, first = find_letter(ls, 0, (1, 'i'))
        if found:
            found, first = find_letter(ls, first, (1, 'j'))
            if found:
                result = 'YES'
    

    
    
    print "Case #%d: %s" % (tc, result)
    #print
    
    
    
