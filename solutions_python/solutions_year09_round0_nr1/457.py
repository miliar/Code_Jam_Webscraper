f = open("A-large.in")

L, D, N = map(int, f.readline().split())

words = set([])
for i in range(D):
    words.add(f.readline()[:-1])

fout = open("A-small.out", 'w')

for case in range(1, N+1):
    patt = f.readline()[:-1]

    bit = 0   
    wordlist = []
    toadd = []
    for c in patt:
        if c == '(':
            bit = 1

        elif c == ')': 
            wordlist.append(toadd)
            toadd = []
            bit = 0

        else:
            if bit:
                toadd.append(c)
            else:
                wordlist.append([c])

    poss = words
    for (i, lets) in enumerate(wordlist):
        new = []
        for let in lets:
            for p in poss:
                if p[i] == let:
                    new.append(p)
        poss = new

    fout.write("Case #%d: %d\n" % (case, len(poss)))

fout.close()

    
            