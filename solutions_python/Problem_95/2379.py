import exceptions as ex
import sys

def getAllTheLetters(begin='a', end='z'):
    beginNum = ord(begin)
    endNum = ord(end)
    for number in xrange(beginNum, endNum+1):
        yield chr(number)

mapping = {}

def improveMap(m, goog, transl):
    for g, t in zip(goog, transl):
        if g == ' ':
            if t != ' ':
                raise ex.Exception('blank to non blank')
        if t == ' ':
            if g != ' ':
                raise ex.Exception('non blank to blank')
        if g in m:
            if m[g] != t:
                raise ex.Exception('inconsistence: ' +
                                   '"' + g + '" was to "' + m[g] + '"' +
                                   ' now "' + t + '"')
        else:
            m[g] = t
    return m
                

mapping = improveMap(mapping,
                     'ejp mysljylc kd kxveddknmc re jsicpdrysi',
                     'our language is impossible to understand')

mapping = improveMap(mapping,
                     'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
                     'there are twenty six factorial possibilities')

mapping = improveMap(mapping,
                     'de kr kd eoya kw aej tysr re ujdr lkgc jv',
                     'so it is okay if you want to just give up')

mapping = improveMap(mapping,
                     'yeq',
                     'aoz')

for letter in getAllTheLetters():
    if not(letter in mapping):
        print 'missing: "' + letter + '"'


allletts = set([l for l in getAllTheLetters()])
allImgs = set(mapping.values())
free = allletts - allImgs

mapping = improveMap(mapping,
                     'z',
                     free)

for letter in getAllTheLetters():
    if not(letter in mapping):
        print 'missing: "' + letter + '"'

infile = sys.argv[1]

infilh = open(infile)
infilh.readline()

outfilh = open('out.txt', 'w')

for cnt, line in enumerate(infilh):
    line = line.rstrip()
    outfilh.write('Case #' + str(cnt+1) + ': ' +
                  ''.join(map(lambda x: mapping[x], line)) + '\n')

infilh.close()
outfilh.close()
