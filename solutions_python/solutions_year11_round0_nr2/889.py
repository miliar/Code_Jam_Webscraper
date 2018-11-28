import sys#, unicodedata
test = sys.stdin.readlines()
#unicodedata.normalize('NFKD', test[0].decode('utf-8')).encode('ascii','ignore')
ncases = int(test[0].rstrip('\n'))
for i in range(1, ncases+1):
    pbm = test[i].rstrip('\n').split(' ')
    ncombi = int(pbm[0])
    combi = {}
    for j in range(ncombi):
        s = pbm[j+1]
        combi[s[0:2]] = s[2]
        combi[s[1]+s[0]] = s[2]
    ncancel = int(pbm[ncombi+1])
    cancel = {}
    for j in range(ncancel):
        s = pbm[j+ncombi+2]
        cancel[s[0:2]] = 1
        cancel[s[1]+s[0]] = 1
    elems = pbm[len(pbm)-1]
    results = []
    last = -1
    for e in elems:
        results.append(e)
        if len(results) > 1:
            #c = e+results[len(results)-1]
            c = results[len(results)-1]+results[len(results)-2]
            while combi.has_key(c):
                results.pop(len(results)-1)
                results[len(results)-1] = combi[c]
                if len(results) > 1:
                    c = results[len(results)-1]+results[len(results)-2]
                else:
                    break
            for k in range(len(results)):
                if cancel.has_key(results[len(results)-1] + results[k]):
                    results = []
                    break
    print "Case #"+str(i)+": [" + ', '.join(results) + "]"
