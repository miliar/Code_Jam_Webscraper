from sys import stdin

DECODE = [[1,2,3,4],[2,-1,4,-3],[3,-4,-1,2],[4,3,-2,-1]]
CODE = {'1': 1, 'i': 2, 'j': 3, 'k': 4}

def readline():
    return tuple(int(i) for i in stdin.readline().rstrip().split())

def multiply(op1, op2):
    return sign(op1)*sign(op2)*DECODE[abs(op1) - 1][abs(op2) - 1]

def power(base, pow):
    product = 1
    pow = pow % 4
    
    while pow > 0:
        product = multiply(product, base)
        pow -= 1
    
    return product

            
def mask(num):
    map = {1: '1', 2: 'i', 3: 'j', 4: 'k'}
    if num >= 0:
        return map[abs(num)]
    else:
        return '-' + map[abs(num)]
        
def code(char):
    return CODE[char]
    
def sign(num):
    if num >= 0:
        return 1
    else:
        return -1
        
        
def search_i_index(L, X, products):    
    if code('i') in products:
        return products.index(code('i'))
    else:
        for pow in range(1, min(X, 4)):
            if power(products[L - 1], pow) == code('i'):
                return (L*pow - 1)
                                
            for index in range(L):
                if multiply(power(products[L - 1], pow), products[index]) == code('i'):
                    return (L*pow - 1) + index
                    
    return None
    

def search_k_index(L, X, rev_products):
    if code('k') in rev_products:
        return rev_products.index(code('k'))
    else:
        for pow in range(1, min(X, 4)):
            if power(rev_products[0], pow) == code('k'):
                return L*(X - pow)
                
            for index in range(-1, -L, -1):                                
                if multiply(rev_products[index], power(rev_products[0], pow)) == code('k'):
                    return L*(X - pow) + index
                    
    return None
    
        
def compute(L, X, original):
    if L*X < 3:
        return False    
    
    new = original*X
    # compute products
    products = [new[0]]
    for index in range(1, len(new)):
        products.append(multiply(products[index - 1], new[index]))
        
    # compute reverse products
    rev_products = [new[-1]]
    for index in range(-2, -len(new) - 1, -1):
        rev_products.insert(0, multiply(new[index], rev_products[index + 1]))        
        
    if products[-1] != -1:
        return False
        
    for i in range(L*X):
        for j in range(i+2, L*X):
            if products[i] == code('i') and rev_products[j] == code('k'):
                return True
    
    return False
            

def main():
    (T,) = readline()

    for case in range(T):
        (L, X) = readline()
        original = [code(char) for char in stdin.readline().rstrip()]
        
        if compute(L, X, original):
            print("Case #%d: YES" % (case + 1))
        else:
            print("Case #%d: NO" % (case + 1))
            
            
        
if __name__ == '__main__':
    main()
