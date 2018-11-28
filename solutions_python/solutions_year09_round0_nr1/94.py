import psyco
psyco.full()

import sys
import re
import os

if len(sys.argv) != 2:
    print 'specify input file'
    exit()
    
with open(sys.argv[1]) as fin:
    lines = fin.readlines()

L,D,N = map(int,lines[0].split())

print L,D,N
words = lines[1:1+D]
patterns = lines[1+D:]

words.sort()

fout = open(os.path.splitext(sys.argv[1])[0]+'.out','wt')
    
for i,pattern in enumerate(patterns):
    print '\b'*10,100*i/len(patterns),'%',
    pattern = pattern.strip()
    regex = re.compile(r'(\w|\(\w{2,}\))')
    tokens = []
    j = 0
    while j < len(pattern):
        m = regex.match(pattern,j)
        if len(m.group()) == 1:
            tokens.append(set(m.group()))
        else:
            tokens.append(set(m.group()[1:-1]))
        j = m.end()
        
    count = 0
    for w in words:
        if all(w[j] in tokens[j] for j in range(L)):
            count += 1
    print>>fout, 'Case #%s: %s'%(i+1,count)
            
    #print tokens
fout.close()    
print

