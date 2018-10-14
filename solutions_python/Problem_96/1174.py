fin = open('2.in', 'r')
fout = open('2.out', 'w')

t = int(fin.readline())
for i in range(t):
    c = 0
    s = map(int, fin.readline().split())
    p3 = s[2] * 3
    
    for j in range(s[0]):
        tj = s[3+j]
        
        if tj > p3 - 3:
            c = c + 1
        elif tj >= p3 - 4 and tj >= 2 and s[1] > 0:
            s[1] = s[1] - 1
            c = c + 1

    fout.write('Case #' + str(i+1) + ': ' + str(c) + '\n')

fin.close()
fout.close()
print 'done!'

