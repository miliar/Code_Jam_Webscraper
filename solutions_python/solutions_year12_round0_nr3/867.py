#Google Code Jam 2012 Qualification Round
#Recycled numbers

import sys

reader = open(sys.argv[1] + '.in', 'r')
writer = open(sys.argv[1] + '.out', 'w')

t = int(reader.readline())

for i in range(t):
    a, b = reader.readline().split()
    a, b = int(a), int(b)
    total = 0
    for j in range(a, b+1):
        n = str(j)
        pairs = []
        for k in range(1, len(n)):
            if int(n[k]) >= int(n[0]):
                m = n[k:] + n[:k]
                if int(m) > int(n) and int(m) <= b:
                    if (n, m) not in pairs:
                        total += 1
                        pairs.append((n, m))                            
    writer.write('Case #%d: %d\n' % (i+1, total))
    
reader.close()
writer.close()
