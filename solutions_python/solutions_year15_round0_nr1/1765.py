fin = open('A-large.in', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())

for i in xrange(t):
    s = fin.readline().split()
    smax = int(s[0])
    
    result = 0
    audience = s[1]
    standing = 0
    for j in xrange(smax + 1):
        if j > standing:
            result = result - standing + j
            standing = j
        standing += int(audience[j])
    
    fout.write('Case #' + str(i + 1) + ': ' + str(result) + '\n')

fout.close()
