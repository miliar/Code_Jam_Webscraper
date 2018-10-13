import sys

import psyco; psyco.full()

def recurse(lines, lang, lineno, count):
    if lineno == len(lines):
        return lang.count(3)
    else:
        lang2 = list(lang)
        count2 = count
        for t in lines[lineno]:
            if lang2[t] == 2:
                count2 += 1
            lang2[t] |= 1
        res1 = recurse(lines, lang2, lineno+1, count2)
        
        lang2 = list(lang)
        count2 = count
        for t in lines[lineno]:
            if lang2[t] == 1:
                count2 += 1
            lang2[t] |= 2
        res2 = recurse(lines, lang2, lineno+1, count2)
        
        return min(res1, res2)
            
def main():
    f = open(sys.argv[1], "rb")
    ncases = int(f.readline())
    for caseno in xrange(ncases):
        known = {}
        count = 0
        lines = []
        nlines = int(f.readline())
        for i in xrange(nlines):
            tok = []
            for t in f.readline().strip().split():
                if t not in known:
                    known[t] = count
                    count += 1
                tok.append(known[t])
            lines.append(tuple(tok))
            
        lang = [0] * count
        #print "x", 2**(nlines-2), count
        count = 0
        for t in lines[0]:
            lang[t] |= 1
        for t in lines[1]:
            if lang[t] == 1:
                count += 1
            lang[t] |= 2
         
        best = recurse(lines, lang, 2, count)
            
        print "Case #%d: %d" % (caseno+1, best)
        
main()