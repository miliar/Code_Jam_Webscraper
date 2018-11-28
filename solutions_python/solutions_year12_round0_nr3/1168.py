fin = open('3.in', 'r')
fout = open('3.out', 'w')

t = int(fin.readline())
for i in range(t):
    c = 0
    t = map(int, fin.readline().split())

    n = t[0]
    j = t[1]
    e = len(str(j)) - 1
    
    if e > 0:
        while n < j:
            l = []
            for k in range(e):
                m = n / (10**(k+1)) + (n % (10**(k+1))) * (10**(e-k))
                if n < m and m <= j and m not in l:
                    l.append(m)
                    c = c + 1
            
            n = n + 1

    fout.write('Case #' + str(i+1) + ': ' + str(c) + '\n')

fin.close()
fout.close()
print 'done!'

