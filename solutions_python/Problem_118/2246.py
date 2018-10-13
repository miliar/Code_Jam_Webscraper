import math
def palindrome(m, n):
    '''returns the number of fair and square palindromes in the range m aand n
       inp - m, n - numbers
       out - num - string'''
    a = int(math.ceil(math.sqrt(m)))
    b = int(math.floor(math.sqrt(n)))
    num = 0
    for i in range(a, b+1):
        j = str(i)
        if j == j[::-1]:
            k = str(i*i)
            if k == k[::-1]:
                num += 1
                # print k
    return str(num)

def readfile(filename):
    f = open(filename, "r")
    all = [line.rstrip() for line in f.readlines()]
    n = int(all[0])
    i = 1
    while i < n + 1:
        x, y = map(int, all[i].split(' '))
        # print x, y
        print 'Case #' + str(i) + ': ' + palindrome(x, y)
        i += 1

readfile('C-small-attempt0.in')
        
        
                
    
    
    
