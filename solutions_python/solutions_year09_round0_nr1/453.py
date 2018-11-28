import sys

LETTERS = set()
WORDS = set()
BYLETTER = None

L = None # word length
D = None # num words
N = None # num patterns


def new_letter(letter):
    global LETTERS, WORDS, BYLETTER, L, D, N
    
    LETTERS.add(letter)

    for i in xrange(0,L):
        BYLETTER[i][letter] = set()


def read_pattern(pat):
    p = []
    i = 0
    l = len(pat)
    while i < l:
        if pat[i] != '(':
            p.append([pat[i]])
        else:
            c = []
            i += 1
            while pat[i] != ')':
                c.append(pat[i])
                if not pat[i] in LETTERS:
                    new_letter(pat[i])
                i += 1
            let = BYLETTER[len(p)]
            c.sort(lambda x,y: len(let[x])-len(let[y]))
            p.append(c)
        i += 1
    return p

def cand_list(pos,li):
    if li == []:
        return set()
#    if pos==4:
#        print "*** "+str(BYLETTER[pos])
    c = set(BYLETTER[pos][li[0]])
    for x in li[1:]:
        c |= BYLETTER[pos][x]
    return c


def pattern(num, pat):
#    print "PATTERN: "+pat
    pat = read_pattern(pat)
    pat = list(enumerate(pat))
    pat.sort(lambda x,y: len(x[1])-len(y[1]))

#    print "INTERNAL: "+str(pat)
    cand = cand_list(pat[0][0],pat[0][1])

#    print "CAND: "+str(cand)

    for pos,lets in pat[1:]:
#        print "CRITERIA: "+str((pos,lets))
#        print "INTERSECT: "+str(cand_list(pos,lets))
        cand &= cand_list(pos,lets)
#        print "CAND: "+str(cand)

    print "Case #%d: %d" % (num,len(cand))


def main():
    global LETTERS, WORDS, BYLETTER, L, D, N

    line = sys.stdin.readline().strip()
    L,D,N = map(int,line.split())

    BYLETTER = [{} for i in xrange(0,L)]

    for i in xrange(0,D):
        word = sys.stdin.readline().strip()
        for j,x in enumerate(word):
            if not x in LETTERS:
                new_letter(x)
            BYLETTER[j][x].add(word)

#    print BYLETTER[4]
#    sys.exit(0)

    for i in xrange(1,N+1):
        pat = sys.stdin.readline().strip()
        pattern(i, pat)


main()
