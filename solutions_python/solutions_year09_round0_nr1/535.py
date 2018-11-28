import re
# h = open('A-small-attempt0.in.txt', 'r')
h = open('A-large.in.txt', 'r')
L, D, N = h.readline().strip().split(' ')
words = []
for i in xrange(int(D)):
    words.append(h.readline().strip())

for i in xrange(int(N)):
    pat = h.readline()
    possible_words = 0
    for word in words:
        pats = re.findall(r'(\w|\(\w+?\))', pat)
        matched = 0
        for j in xrange(len(pats)):
            pp = pats[j]
            if pp.startswith("("):
                pp = pp[1:]
            if pp.endswith(")"):
                pp = pp[:-1]
            
            if word[j] in pp:
                matched += 1
        
        if matched == len(word):
            possible_words += 1
    
    print "Case #%s: %s" % (i+1, possible_words)
            
            

h.close()