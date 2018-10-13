import os
import re

handle = open('A-large.in','r')
outHandle = open('LargeInput.txt', 'w')

line = handle.readline()
line = line.replace('\n', '')
p1 = line.partition(' ')
p2 = p1[2].partition(' ')
L = p1[0]
D = p2[0]
N = p2[2]

print L, N, D
words = []

for i in range(0, int(D)):
    line = handle.readline()
    line = line.replace('\n', '')
    words.append(line)
patterns = []

for i in range(0, int(N)):
    line = handle.readline()
    line = line.replace('\n', '')
    patterns.append(line)

counts = []

for i in range(0, int(N)):
    counts.insert(i, int(0))

#for each pattern
for i in range(0, int(N)):
    print i
    pattern = patterns[i].replace(')',']')
    pattern = pattern.replace('(','[')
    for j in range(0,int(D)):
        found = re.match(pattern, words[j])
        if found:
            counts[i] = counts[i] + 1

for i in range(0, int(N)):
    outHandle.write('Case #' + str(i+1) + ': ' + str(counts[i]) + '\n')
    
