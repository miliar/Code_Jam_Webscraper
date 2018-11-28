import re


f = open("s.txt", 'r')
l, d, n =  [int(i) for i in f.readline().split()]

words = []
pattern = []
count = 0
for i in f:
    if count < d:
        words.append(i[:-1])
    else:
        pattern.append(i[:-1].replace('(','[').replace(')',']'))
    count += 1
        
#print words
#print len(words)
#print pattern
#print len(pattern)
    
f.close()
for c, p in enumerate(pattern):
    head = []
    count = 0
    pat = re.compile(p)
    if p[0] != '[':
        head = [p[0]]
    else:
        for i in p[1:]:
            if i==']': break
            head.append(i)
    for w in words:
        if not w[0] in  head: continue
        mat = pat.match(w)
        if mat != None:
            count += 1
    print 'Case #'+str(c+1)+':', count
