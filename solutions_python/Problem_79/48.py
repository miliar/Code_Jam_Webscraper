#!/usr/bin/python
def match(word, guess, alrdy_letters):
    return reduce(bool.__and__, map(lambda a:(a[1]=="." and a[0] not in alrdy_letters) or a[0] == a[1],zip(word,guess)))

def points(D, word, strat):
    D = [x for x in D if len(x) == len(word)]
    guess = "."*len(word)
    ret = 0
    idx = 0
    alrdy_letters = set()
    while guess!=word:
        letters = set()
        for w in D:
            for l in w:
                letters.add(l)
        while strat[idx] not in letters:
            idx += 1
        let = strat[idx]
        alrdy_letters.add(let)
        idx += 1
        point = True
        newguess = ""
        for x in xrange(len(word)):
            if word[x] == let:
                point = False
                newguess += let
            else:
                newguess += guess[x]
        guess = newguess
        if point:
            ret += 1
            D = [x for x in D if let not in x]
        D = [x for x in D if match(x, guess,alrdy_letters)]
        #print let +" "+guess +" "+str(D)+" "+reduce(lambda a,b:a+b,list(letters))
    return ret

T = int(raw_input())
for QQ in xrange(1,T+1):
    N,M = map(int,raw_input().split(" "))
    D = []
    for x in xrange(N):
        D.append(raw_input())
    ret = ""
    for i in xrange(M):
        strat = raw_input()
        best = -9000
        best_word = "prolich"
        #print strat
        for word in D:
            candidate = points(D,word,strat)
            #print "%s gives %s points" % (word, candidate)
            if candidate > best:
                best = candidate
                best_word = word
        ret += " "+best_word

    print "Case #"+str(QQ)+":"+ret
