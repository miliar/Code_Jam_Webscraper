fin = file("C-small-attempt0.in", "rU")
fout = file("C-small-attempt0.out", "w")

nruns = int(fin.readline().strip())
for i in xrange(nruns):
    line = fin.readline().strip().split()
    nplayers = int(line[0])
    lownote = int(line[1])
    highnote = int(line[2])

    othernotes = fin.readline().strip().split()

    outnote = -1
    for note in xrange(lownote, highnote+1):
        possible = 1
        for othern in othernotes:
            othern = int(othern)
            if othern % note == 0 or note % othern == 0:
                continue #harmony
            else:
                possible = 0
                break
        if possible == 1:
            outnote = note
            break
    if outnote != -1:
        result = outnote
    else:
        result = 'NO'
    strout = "Case #" + str(i+1) + ": " + str(result) + "\n"
    #print strout
    fout.write(strout)
fin.close()
fout.close()
