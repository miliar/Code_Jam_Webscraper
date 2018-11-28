

def palindrome(num):
    ## Checks whether a is palindrome or not.
    #  Returns True if palindrome, False otherwise.
    temp = num
    s = 0
    while num:
        r = num%10
        num = num/10
        s = s*10 + r
        #print num,s

    if temp == s:
        return True
    else:
        return False

def perfectsqr(n):
    a = pow(n, 0.5)
    b = int(a)
    if b*b == n:
        return True
    else:
        return False


def howMany(l):   #(A,B):
    ## Counts the number of fair and square numbers >= A and <= B.
    A = l[0]
    B = l[1]

    x = []
    a = pow(A, 0.5)
    b = pow(B, 0.5)
    if perfectsqr(A):
        p = int(a)
    else:
        p = int(a) + 1
    q = int(b)
    for i in xrange(p, q + 1):
        if palindrome(i):
            x += [i*i]

    return len(filter(palindrome, x))

    ## Now filter out the palindromes...



f = open('Csmall.in','r')
a = f.read()
b = a.split('\n')

del(b[-1])
f.close()


g = open('CsmallOut','w')




T = int(b[0])
for i in xrange(1, T + 1):
    b[i] = list(map(int,b[i].split(' ')))
    s = str(howMany(b[i]))
    w = 'Case #%d: %s \n' % (i,s)
    print w
    g.write(w)
g.close()



