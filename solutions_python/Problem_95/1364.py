gg = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
    'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
    'de kr kd eoya kw aej tysr re ujdr lkgc jv']
    
eng = ['our language is impossible to understand',
    'there are twenty six factorial possibilities',
    'so it is okay if you want to just give up']
    
translateMap = {'q':'z','z':'q'}

for i in range(3):
    for x,y in zip(list(gg[i]),list(eng[i])):
        translateMap[x] = y

for i in range(int(raw_input(""))):
    print 'Case #%d:'%(i+1),''.join(map(lambda x: translateMap[x], list(raw_input(''))))