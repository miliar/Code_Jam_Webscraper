# -*- coding: utf-8 -*-
        
        
helper = {
    '1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'},
    'i': {'1': 'i', 'i': (-1, '1'), 'j': 'k', 'k': (-1, 'j')},
    'j': {'1': 'j', 'i': (-1, 'k'), 'j': (-1, '1'), 'k': 'i'},
    'k': {'1': 'k', 'i': 'j', 'j': (-1, 'i'), 'k': (-1, '1')}
}

def quatMult(a, b):
    sa = sb = 1
    if len(a) == 2:
        sa, a = a
    if len(b) == 2:
        sb, b = b
        
    tmp = helper[a][b]
    if len(tmp) == 2:
        return (sa * sb * tmp[0], tmp[1])
    return (sa * sb, tmp)
        
    
result = {True: "YES", False: "NO"} 
def case(L, X, string):

    product = (1, '1')
    cycle = X
    for repetition in xrange(X):
        for char in string:
            product = quatMult(product, char)
        if product == (1, '1'):
            cycle = repetition + 1
            break
            
    simple = X % cycle
    
    foundI = foundK = False
    newproduct = (1, '1')
    for repetition in xrange(cycle * 2):
        for char in string:
            newproduct = quatMult(newproduct, char)
            if newproduct == (1, 'i'):
                foundI = True
            if foundI and newproduct == (1, 'k'):
                foundK = True
             
    if simple > 0:
        product = (1, '1')
        for repetition in xrange(simple):
            for char in string:
                product = quatMult(product, char)
                
    return result[foundI and foundK and product == (-1, '1')]
    

def fromStdin():
    while True:
        yield raw_input()

def main():
    feed = fromStdin()
    T = int(next(feed))
    for caz in xrange(T):
        L, X = [int(i) for i in next(feed).split()]
        string = [c for c in next(feed) if c not in '\r\n']
        rep = case(L, X, string)
        print "Case #{}: {}".format(caz+1, rep)

if __name__ == "__main__":
    main()
