trainingG = ["ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
trainingS = ["our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"]

def getConversionArray(G,S):
    translationDict = {}
    for k in range(0,len(G)):
        translated = G[k];
        normal = S[k];
        for i in range(0,len(translated)):
            if (translated[i] is not ' '):
                translationDict[translated[i]] = normal[i];
    return translationDict


conversionArray = getConversionArray(trainingG, trainingS)
conversionArray['z']='q'
conversionArray['q']='z'
ncases = int(raw_input())
for k in range(0,ncases):
    googlonesePhrase = raw_input()
    normalPhrase = ""
    for i in range(0,len(googlonesePhrase)):
        if (googlonesePhrase[i] is not ' '):
            normalPhrase+=conversionArray[googlonesePhrase[i]]
        else:
            normalPhrase+=' '
    print "Case #{0}: {1}".format(k+1,normalPhrase)