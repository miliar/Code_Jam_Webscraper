def tail(list,t):
    for c,i in enumerate(list):
        if i>t:
            return list[c:]
    return []

f = open("cs.in", 'r')
n =  int(f.readline())

text="welcome to code jam"
index="welcomtdja "
cw = len(text)-1

case = 0
for line in f:
    case += 1
    wdic = {}
    line=line[:-1]
    for c, w in enumerate(line):
        for i in index:
            if i==w:
                if wdic.has_key(i):
                    wdic[i].append(c)
                else:
                    wdic[i] = [c]
    if len(wdic) < len(index):
        print "Case #%d: 0000"%case
        continue
    
    count = 0
    for a in wdic[text[0]]:
        for b in tail(wdic[text[1]], a):
            for c in tail(wdic[text[2]], b):
                for d in tail(wdic[text[3]], c):
                    for e in tail(wdic[text[4]], d):
                        for f in tail(wdic[text[5]], e):
                            for g in tail(wdic[text[6]], f):
                                for h in tail(wdic[text[7]], g):
                                    for i in tail(wdic[text[8]], h):
                                        for j in tail(wdic[text[9]], i):
                                            for k in tail(wdic[text[10]], j):
                                                for l in tail(wdic[text[11]], k):
                                                    for m in tail(wdic[text[12]], l):
                                                        for n in tail(wdic[text[13]], m):
                                                            for o in tail(wdic[text[14]], n):
                                                                for p in tail(wdic[text[15]], o):
                                                                    for q in tail(wdic[text[16]], p):
                                                                        for r in tail(wdic[text[17]], q):
                                                                            count+= len(tail(wdic[text[18]], r))
    print "Case #%d: "%case+str(count%10000).zfill(4)
