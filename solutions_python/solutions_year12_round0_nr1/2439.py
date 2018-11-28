def genAlph(googlerese, english):
    googleToEnglish = {}
    for x,y in zip(googlerese,english):
        googleToEnglish[x] = y
    return googleToEnglish

alph = dict(genAlph("ejp mysljylc kd kxveddknmc re jsicpdrysi", 
                    "our language is impossible to understand").items()
          + genAlph("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                    "there are twenty six factorial possibilities").items()
          + genAlph("de kr kd eoya kw aej tysr re ujdr lkgc jv zq",
                    "so it is okay if you want to just give up qz").items())

nb = int(raw_input())
sentences = {}
for i in range(1,nb+1):
    sentences[i] = ''.join([alph[l] for l in str(raw_input())])

for n,r in sentences.items():
    print "Case #"+str(n)+": "+r
