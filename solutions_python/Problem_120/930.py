import math

fin = open('A-small-attempt0.in', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())

for i in xrange(t):
    r, paint = map(int, fin.readline().split())
    if paint >= 4*r + 6:
        D = 4*r*r - 2*r + 1 + 8*paint
        if D >= 0:
            n = int((float(-2*r) + float(1) + float(math.sqrt(D)))/4)
            if float(4*r + 2 + 4*(n - 1))/2.0*n > paint:
                n -= 1
        else:
            n = 1
    else:
        n = 1
    fout.write('Case #' + str(i + 1) + ': ' + str(n) + '\n')

fout.close()
