# Has been a great while since I coded...Here Goes
# Alien Language
# Usage pretty simple: Q1.py <inputfile>
# requires a EOF to terminate


#Read Input - Absolutely 0 input checks

import fileinput

infile = fileinput.input()

params = infile.readline()

L,D,N = [int(p) for p in params.split()]

# Build the dictionary
d,n = 0,0
words = []
cases = []
letter = []
newwords = []
wordsdict = []
gotparen = False

def getnewwords():
    global words, newwords, letter
#    print "In getwords"
#    print words
#    print letter
    for word in words:
        if len(word) < 1:
            return
        if word[0] in letter:
            newwords.append(word[1:])
    words = newwords
    newwords = []
        
while d < D:
    words.append(infile.readline().strip())
    d += 1

while n < N:
    cases.append(infile.readline().strip())
    n += 1

infile.close()

wordsdict = words

n = 1
for word in cases:
    words = wordsdict
    for ch in word:
        if ch == ')' and gotparen == True:
            gotparen = False
            getnewwords()
            letter = []
        elif ch == '(':
            letter = []
            gotparen = True
        elif ch.islower():
            letter.append(ch)
            if not gotparen:
                getnewwords()
                letter = []
        else:
            print "Something Wrong\n"
    print "Case #%d: %d" % (n,len(words))
    n += 1

#print words
#print wordsdict