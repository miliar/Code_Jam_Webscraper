'''
Created on Apr 14, 2012

@author: herman
'''

from string import split

infile = open("small_input.txt","r")
outfile = open("small_output.txt","w")

# need to establish mapping
# 'a' = 0
Gmap = [0 for x in xrange(26)]
Gtouched = [0 for x in xrange(26)]
Stouched = [0 for x in xrange(26)]

Gmap[ord('y') - ord('a')] = 0
Gmap[ord('e') - ord('a')] = ord('o') - ord('a')
Gmap[ord('q') - ord('a')] = ord('z') - ord('a')

Gtouched[ord('q') - ord('a')] = 1
Stouched[ord('z') - ord('a')] = 1

Gtext = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
Stext = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

Gwords = Gtext.split()
Swords = Stext.split()

for w in xrange(len(Gwords)):
    for c in xrange(len(Gwords[w])):
        Gmap[ord(Gwords[w][c]) - ord('a')] = ord(Swords[w][c]) - ord('a')
        Gtouched[ord(Gwords[w][c]) - ord('a')] = 1
        Stouched[ord(Swords[w][c]) - ord('a')] = 1
        
Gmap[Gtouched.index(0)] = Stouched.index(0)

for w in xrange(26):
    print "%c -> %c\n" % (chr(w + ord('a')),chr(Gmap[w] + ord('a')))

trials = int(infile.readline())

def trans(Gword):
    Sword = ''
    for w in xrange(len(Gword)):
        Sword += chr(Gmap[ord(Gword[w]) - ord('a')] + ord('a'))
    return Sword

for i in xrange(trials):
    G = infile.readline()
    Sws = []
    for w in G.split():
        Sws.append(trans(w))
    space = ' '

    S = space.join(Sws)
    
    str = "Case #%d: %s\n" % ((i+1),S)
    print str
    outfile.write(str)

infile.close()
outfile.close()
    