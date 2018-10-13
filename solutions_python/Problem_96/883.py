#Google Code Jam 2012 Qualification Round
#Dancing with the Googlers

import sys

reader = open(sys.argv[1] + '.in', 'r')
writer = open(sys.argv[1] + '.out', 'w')

t = int(reader.readline())

for i in range(t):
    line = reader.readline().split()
    s = int(line[1])
    p = int(line[2])
    points = []
    max_scores = 0
    max_temp = 0
    
    for j in range(3, len(line)): points.append(int(line[j]))

    if p < 2:
        min_non_sur = p
        min_sur = p
    else:
        min_non_sur = p + (p-1)*2
        min_sur = p + (p-2)*2

    for j in range(len(points)):
        if points[j] >= min_non_sur: max_scores += 1
        elif points[j] >= min_sur: max_temp += 1
        
    max_scores += min(s, max_temp)
    writer.write('Case #%d: %d\n' % (i+1, max_scores))
    
reader.close()
writer.close()
