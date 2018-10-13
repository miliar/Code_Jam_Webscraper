import sys, re
input = open(sys.argv[1])
data = input.readlines()
L, D, N = data[0].split()
L, D, N = int(L), int(D), int(N)
known = set()

def parser(line):
    res = []
    i = 0
    while i < len(line):
        if line[i] == '(':
            part = ''
            i+=1
            while line[i] != ')':
                part += line[i]
                i+=1
            res.append(set(part))
            i+=1
        else:
            res.append(set(line[i]))
            i+=1
    return res

for i in xrange(1, D+1):
    line = data[i].strip()
    known.add(line)

for i in xrange(D+1, D+N+1):
    bits = parser(data[i].strip())
    word_hits = 0
    for word in known:
        char_hits = 0
        for j, char in enumerate(word):
            if char in bits[j]:
                char_hits += 1
        if char_hits == L:
            word_hits += 1
    print 'Case #%i: %i' % (i-D, word_hits)
