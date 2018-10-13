import string
import sys

numCases = int(raw_input())

for case in xrange(1, numCases + 1):
    size = int(raw_input())
    word = raw_input()
    
    subSets = []
    for i in xrange(0, len(word), size):
        subSets.append(word[i: i + size])
    
    keys = []
    generated = []
    for i in xrange(size):
        generated.append(0)
        
    while generated[-1] != size:
        key = []
        for i in xrange(size):
            key.append(generated[i])
            
        valid = True
        for i in xrange(size):
            valid = valid and key.count(i) == 1
        if valid:
            keys.append(key)
        generated[0] += 1
        for i in xrange(size - 1):
            if generated[i] == size:
                generated[i] = 0
                generated[i + 1] += 1
                
            
    compress = sys.maxint
    for k in keys:
        count = 0
        last = None
        for s in subSets:
            for i in xrange(len(key)):
                if s[k[i]] != last:
                    count += 1
                    last = s[k[i]]
                    
        if count < compress:
            compress = count
            
    print "Case #%d: %d" % (case, compress)