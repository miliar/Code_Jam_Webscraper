def gcd (a, b):
    if a % b == 0:
        return b
    else:
        return gcd (b, a % b)
    

def solution (x):
    '''x is in the form a/b'''
    num, den = map (int, x.split('/'))
    GCD = gcd (num, den)
    num = num / GCD
    den = den / GCD
    i = 0
    if num > den:
        return 'impossible'
    while 2 ** i < den:
        i += 1
        #print den, i ** 2
    #print i, num, den    
    if 2 ** i > den:
        return 'impossible'
    if num == den:
        return str(0)
    i = 0
    while i <= 40:
        if ((num * (2 ** i)) / float (den)) - 1 >= 0:
            return str(i)
        i += 1
    return 'impossible'    
    

f = open ('input.txt', 'r')
g = open ('output.txt', 'w')
N = int (f.readline())
for case in xrange (1, N + 1):
    x = filter (lambda x : x != '\n', f.readline())
    sol = solution (x)
    print sol
    g.write ('Case #' + str (case) + ': ' + sol + '\n')
g.close()
f.close()


