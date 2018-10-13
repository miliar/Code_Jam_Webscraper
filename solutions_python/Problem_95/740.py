engLetters = map(chr, range(97, 123))
eng = 'a zoo ' + 'our language is impossible to understand ' + 'there are twenty six factorial possibilities ' + 'so it is okay if you want to just give up'
gooLetters = map(chr, range(97, 123))
goo = 'y qee ' + 'ejp mysljylc kd kxveddknmc re jsicpdrysi ' + 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd ' + 'de kr kd eoya kw aej tysr re ujdr lkgc jv'

dictGooEng = {}
unMappedLetters = []
for e in engLetters:
    i = eng.find(e)
    if i > -1:    
        dictGooEng[goo[i]] = e
        gooLetters.remove(goo[i])
    else:
        unMappedLetters.append(e)

dictGooEng[gooLetters[0]] = unMappedLetters[0]
dictGooEng[' '] = ' '
dictGooEng['\n'] = '\n'
f = open('A-small-attempt0.in', 'r')
f2 = open('A-small-attempt0.out','w')
numOfCases = int(f.readline())

for case in range(numOfCases):
    googlish = f.readline()
    english = []
    for c in googlish:
       # english.append(dictGooEng.setdefault(c, " "))
        english.append(dictGooEng[c])
    result = 'Case #' + repr(case + 1) + ": " + "".join(english)
    #print result
    f2.write(result)
f.close()
f2.close()
