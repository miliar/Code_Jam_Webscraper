import string

f = open('A-small-attempt0.in', 'r')
g = open('output.txt', 'w')

n = int(f.readline())
count = 1

while count <= n:
    b = set()

    a = int(f.readline()[:-1])
    for i in xrange(4):
        line = string.split(f.readline()[:-1])
        if i == a - 1:            
            b = set([int(x) for x in line])
        
    a = int(f.readline()[:-1])
    for i in xrange(4):
        line = string.split(f.readline()[:-1])
        if i == a - 1:
            c = set([int(x) for x in line])
            intersect = list(c.intersection(b))
            l = len(intersect)
            if l == 1:
                g.write("Case #%d: %d\n" % (count, intersect[0]))
            elif l > 1:
                g.write("Case #%d: Bad magician!\n" % count)
            else:
                g.write("Case #%d: Volunteer cheated!\n" % count)

    count += 1
    
f.close()
g.close()