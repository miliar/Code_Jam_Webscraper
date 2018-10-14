import math

def reverseNumber(n, partial=0):
    if n == 0:
        return partial
    return reverseNumber(n / 10, partial * 10 + n % 10)

def isPalidrome(n):
    return n == reverseNumber(n)


type = 'small'
fi = open('C-%s.in' % type, 'r')
fo = open('C-%s.out' % type, 'wb')
num_games = int(fi.readline())

for T in xrange(1, num_games + 1):
    # Simple optimization, loop through square roots
    A, B = fi.readline().rstrip('\n').split(' ')
    start = int(math.ceil(math.sqrt(int(A))))
    end = int(math.floor(math.sqrt(int(B))))
    num = 0
    for i in xrange(start, end + 1):
        if ((isPalidrome(i)) and (isPalidrome(i*i))):
            num += 1

    # Output message
    output = 'Case #%d: %d' % (T, num)
    fo.write('%s\n' % output)


fi.close()
fo.close()