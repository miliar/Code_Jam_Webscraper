from math import sqrt

f = open('C-small-attempt0.in')
out = open('out', 'w')

n = int(f.readline())

def is_palin(n):
    s = str(n)
    for i in xrange(len(s)/2):
        if s[i] != s[-(i+1)]:
            return False
    return True

for i in xrange(1, n+1):
    x, y = f.readline().strip().split()
    x,y = int(x), int(y)

    #a, b = int(sqrt(int(x))), int(sqrt(int(y)))
    num = 0

    for j in xrange(x, y+1):
        blah = int(sqrt(j))
        if blah*blah == j and is_palin(j) and is_palin(blah):
            num += 1

    out.write('Case #' + str(i) + ': ' + str(num) + '\n')
    


