import re, sys

mapping = {}
strMap = {'ejp mysljylc kd kxveddknmc re jsicpdrysi' : 'our language is impossible to understand',
          'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd' : 'there are twenty six factorial possibilities',
          'de kr kd eoya kw aej tysr re ujdr lkgc jv' : 'so it is okay if you want to just give up'
          }
for (key, value) in strMap.iteritems():
    for i in xrange(len(key)):
        if (key[i] != ' '):
            mapping[key[i]] = value[i]
mapping['q'] = 'z'
mapping['z'] = 'q'

def coreCalc(data):
    result = []
    for i in xrange(len(data)):
        word = data[i]
        newWord = []
        for j in xrange(len(word)):
            letter = word[j]
            if letter in mapping:
                newWord.append(mapping[letter])
        result.append(''.join(newWord))
    return ' '.join(result)
            
N = int(sys.stdin.readline().strip())
for qw in range(1, N + 1):
    print 'Case #%d:' % qw,

    data = sys.stdin.readline().strip().split()
    result = coreCalc(data)
    print result.strip()
