from sys import stdin

def isPalindrome(n):
    n = str(n)
    l = len(n) / 2
    for i in range(l):
        if n[i] != n[-i-1]:
            return False
    return True

def getNewBounds(a, b):
    x = int(a ** 0.5)
    if x ** 2 < a:
        x += 1
    y = int(b ** 0.5)
    return x, y

def findNums(a, b):
    x, y = getNewBounds(a, b)
    count = 0
    for i in range(x, y+1):
        if isPalindrome(i):
            j = i ** 2
            if isPalindrome(j):
                count += 1
    return count

stdin.readline()
count = 0
for line in stdin:
    count += 1
    line = line.strip('\n')
    print 'Case #%r: %r' % (count, findNums(int(line.split(' ')[0]), int(line.split(' ')[1])))