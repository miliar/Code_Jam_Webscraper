import os

def get_input():
    
    fil = open('killerword.in')
    lines = fil.readlines()
    ar = []
    no = 1
    cases = int(lines[0])
    for x in xrange(0,cases):
        cas = []
        n,m = map(int, lines[no].split(" "))
        no = no + 1
        sts = [lin.replace('\n','') for lin in lines[no:no+n]]
        cas.append(sts)
        no = no + n
        sts = [lin.replace('\n','') for lin in lines[no:no+m]]
        no = no + m
        cas.append(sts)
        ar.append(cas)
    return ar

def subcase(word, words, strat):

    def match(ptn, guessed, w):
        
        for i,c in enumerate(w):
            
            if ptn[i] == '_' and c not in guessed:
                continue
            if ptn[i] == '_' and c in guessed:
                return False
            if ptn[i] != c:
                return False
        
        return True

    numblanks = len(word)
    wd = ['_'] * numblanks
    rem = [x for x in words if len(x) == numblanks]
    pts = 0
    #print 'Rem at start = %s' % rem
    guessed = set()
    for c in strat:
        
        if len(rem) == 1:
            return pts
            
        #print 'c = %s' % c
        remset = set()
        for w in rem:
            lts = [x for x in w]
            remset = remset | set(lts)
        if c not in remset:
            #print 'Skipping %s' % c
            continue
        guessed = guessed | set([c])
            
        oldwd = wd
        wd = [c if word[x] == c else wd[x] for x in xrange(0, numblanks)]
        if wd == oldwd:
            #print 'Lost a point'
            pts = pts + 1
            
        rem = [x for x in rem if match(wd, guessed, x)]
        
        #print wd, rem
    return pts

def case(words, strats):
    
    def fn(w):
        
        for x in xrange(0, len(words)):
            if words[x] == w:
                return x
    
    ans = []
    for strat in strats:
        maxs = -1
        maxwd = ''
        choices = []
        for word in words:
            #print 'Subcase %s %s' % (word, strat)
            mx = subcase(word, words, strat)
            #print 'Got Result: %s' % mx
            if mx > maxs:
                maxs = mx
                choices = [word]
            elif mx == maxs:
                choices.append(word)
        idx = map(fn, choices)
        idx.sort()
        #print idx
        choices = [words[x] for x in idx]
        #print choices
        maxwd = choices[0]
        ans.append(maxwd)
        
    return ans

def main():
    
    inps = get_input()
    #print inps
    x = 0
    out = open('killerword.out', 'w')
    for inp in inps:
        #print inp
        x = x + 1
        cas = case(*inp)
        ans = ' '.join(cas)
        st = 'Case #%s: %s' % (x, ans)
        print st
        print>>out, st

if __name__ == "__main__":
    
    main()
