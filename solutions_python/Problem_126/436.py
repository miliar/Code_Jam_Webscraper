#fin = file("A-small-eg.in", "rU")
#fout = file("A-small-eg.out", "w")
fin = file("A-small-attempt0.in", "rU")
fout = file("A-small-attempt0.out", "w")
#fin = file("A-large.in", "rU")
#fout = file("A-large.out", "w")

nruns = int(fin.readline().strip())
for i in xrange(nruns):
    line = fin.readline().strip().split()
    word = line[0]
    nconsec = int(line[1])

    isvowel = []
    subcount = 0
    wlen = len(word)

    for j in word:
        if j in 'aeiou':
            isvowel.append(1)
        else:
            isvowel.append(0)

    #print word, isvowel
    for sublen in xrange(nconsec, wlen+1): #substring lengths
        #print 'sublen =', sublen, 'wlen = ', wlen
        for spos in xrange(0, wlen-sublen+1):
            conseccons = 0
            #print 'sublen =', sublen
            #print 'spos =', spos
            for k in xrange(spos, spos+sublen):
                if isvowel[k] == 0:
                    conseccons += 1
                else:
                    conseccons = 0
                if conseccons >= nconsec:
                    break
            if conseccons >= nconsec:
                subcount += 1

    result = subcount

    strout = "Case #" + str(i+1) + ": " + str(result) + "\n"
    #print strout
    fout.write(strout)
fin.close()
fout.close()
