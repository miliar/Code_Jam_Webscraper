fin = open('D-large.in', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())

for i in xrange(t):
    n = int(fin.readline())
    bricks = map(float, fin.readline().split())
    bricks2 = map(float, fin.readline().split())
    bricks.sort(reverse = True)
    bricks2.sort(reverse = True)
    a = 0
    b = 0
    result = 0
    while b < n:
        if bricks[a] > bricks2[b]:
            a += 1
            b += 1
            result += 1
        else:
            b += 1

    a = 0
    b = 0
    result2 = 0
    while a < n:
        if bricks[a] < bricks2[b]:
            a += 1
            b += 1
            result2 += 1
        else:
            a += 1
            
    
    fout.write('Case #' + str(i + 1) + ': ' + str(result) + ' ' + str(n - result2) +  '\n')

fout.close()

