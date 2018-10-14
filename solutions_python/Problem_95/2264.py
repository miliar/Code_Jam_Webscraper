
import sys

googlerese = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"

english = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

d = {} 

for i,letter in enumerate(googlerese):
    d[letter] = english[i]

d['z'] = 'q'
d['q'] = 'z'

f = open(sys.argv[1],'r')

numLines = int(f.readline())

#print numLines

for i in range(1,numLines+1):

    inputString = f.readline()

    result = map(lambda x: d[x], inputString.rstrip('\n'))

    result = ''.join(result)

    print 'Case #' + str(i) + ': '+ result
