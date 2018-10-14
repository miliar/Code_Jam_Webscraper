from itertools import product

def isPalindrome(n):
    return list(str(n)) == list(reversed(str(n)))

def squareIsFairAndSquare(n):
    return isPalindrome(n) and isPalindrome(n*n)


def fun(h):
    for i, j, k in product(*[range(h+1)]*3):
        yi = [0]*h
        if i < h:  yi[i] = 1
        if j < h:  yi[j] = 1
        if k < h:  yi[k] = 1
        yield yi

                

#for n in range(1, 10000000):
    #if squareIsFairAndSquare(n):
        #print(n)

# all palindromes with 'k' digits
# that only consists of numbers '0, 1' 
# or '2' in the middle or on the edges
# k > 1
def palindromes(k):
    if k%2 == 0:
        h = k//2-1
        for p in fun(h): #product(*[range(2)]*h):
            yield int(''.join(map(str, [1] + list(reversed(p)) + list(p) + [1])))
            yield int(''.join(map(str, [2] + list(reversed(p)) + list(p) + [2])))
                
    elif k == 1:
        for i in range(1, 4): 
            yield i
    else: 
        for middle in range(0, 3):
            h = (k-1)//2-1
            for p in fun(h): # product(*[range(2)]*h):
                yield int(''.join(map(str, [1] + list(reversed(p)) + [middle] + list(p) + [1] )))
                yield int(''.join(map(str, [2] + list(reversed(p)) + [middle] + list(p) + [2] )))
def digitSum(n):
    return sum(map(int, str(n)))

ln = dict()

fairAndSquare = set()
for k in range(1, 51):
    for p in palindromes(k):
        if isPalindrome(p*p):
            fairAndSquare.add(p*p)

    #print()
    #for p in sorted(fairAndSquare):
        #print(p)
    #ln[k] = len(fairAndSquare)


#for i in sorted(ln.keys()):
    #print("{} of length {}".format(ln[i], i))
    
T = int(input())
for test in range(T):
    a, b = map(int, input().split(' '))
    ans = set()
    for fas in fairAndSquare:
        if a <= fas <= b:
            ans.add(fas)
    print( "Case #{}: {}".format(test+1, len(ans)))
