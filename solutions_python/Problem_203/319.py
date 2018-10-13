
    
def copy(cake, src, dst):
    #print "Copy from %d to %d" % (src, dst)
    for i in range(len(cake[0])):
        cake[dst][i] = cake[src][i]

def transform(cake, r, c):
    last_letter = c+1
    last_row = r+1
    for i in range(r):
        if cake[i].count('?') < c:
            for j in range(c):
                if cake[i][j] != '?':
                    last_letter = j
                    k = j-1
                    #print "expanding %s backwards" % (cake[i][j])
                    while k >= 0 and cake[i][k] == '?':
                        cake[i][k] = cake[i][j]
                        k -= 1
            for k in range(last_letter+1, c):
                cake[i][k] = cake[i][last_letter]
    for i in range(r):
        if cake[i][0] != '?':
            last_row = i
            j = i-1
            #print "expanding line %s backwards from %d" % (cake[i], i)
            while j >= 0 and cake[j][0] == '?':
                copy(cake, i, j)
                j -= 1
    for j in range(last_row+1, r):
        copy(cake, last_row, j)

t = int(raw_input())
for i in xrange(1, t + 1):
    line = raw_input()
    (r, c) = map(lambda x: int(x), line.split(' '))
    cake = []
    for j in range(r):
        line = raw_input()
        cake.append(list(line))
    
    transform(cake, r, c)
    print "Case #{}:".format(i)
    for i in range(r):
        print ''.join(cake[i])
