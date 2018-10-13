import sys


def assemble(s, X):
    if X < 14:
        return X * s
    else:
        return min(X, 14 + (X - 14) % 4) * s

def multiply(a, b):
#    print(a, b, end='')

    minus = False
    if a[0] == '-':
        minus = not minus
        a = a[1:]

    if b[0] == '-':
        minus = not minus
        b = b[1:]

    result = ''

    if a == b:
        result = '1'
        minus = not minus
    elif a == '1':
        result = b
    elif b == '1':
        result = a   
    elif (a == 'i') and (b == 'j'):
        result = 'k'
    elif (a == 'i') and (b == 'k'):
        result = 'j'
        minus = not minus
    elif (a == 'j') and (b == 'i'):
        result = 'k'
        minus = not minus
    elif (a == 'j') and (b == 'k'):
        result = 'i'
    elif (a == 'k') and (b == 'i'):
        result = 'j'
    elif (a == 'k') and (b == 'j'):
        result = 'i'
        minus = not minus
    else:
        print('Unsupported combination: ', a, b)
        sys.exit()

#    print(' ', ('-' if minus else ''), result)

    if minus:
        return '-' + result
    else:
        return result
    

def find_k(s, i0, cache):

    if i0 in cache:
        return cache[i0]
        
    symbol = s[i0]

    for i in range(i0 + 1, len(s)):
        symbol = multiply(symbol, s[i])

#    print('k[', i0, ']: ', s[i0:], ' => ', symbol)

    result = symbol == 'k'

    cache[i0] = result

    return result

def find_jk(s, i0, cache):
    if i0 == len(s):
        return False

    symbol = s[i0]

    for i in range(i0 + 1, len(s)):
        if symbol == 'j':
            if find_k(s, i, cache):
                return True

        symbol = multiply(symbol, s[i])

    #print('jk: ', s[i0:], ': fail')

    return False

def find_ijk(s):
    symbol = s[0]

    cache = dict()

    for i in range(1, len(s)):
#        print(symbol)
        if symbol == 'i':
#            print(i)
            if find_jk(s, i, cache):
                return True

        symbol = multiply(symbol, s[i])

    return False


def solve(s):
#    print(s)
    if len(s) == 0:
        return False

    return find_ijk(s)
    

T = int(input())

for i in range(1, T + 1):
    
    L, X =[int(s) for s in input().split()]
    
    s = input()

    result = solve(assemble(s, X))

    print("Case #", i, ": ", ('YES' if result else 'NO'), sep='')


