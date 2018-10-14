fin = file("A-large.in.txt", "rU")
fout = file("A-large.out.txt", "w")

nruns = int(fin.readline().strip())
for i in xrange(nruns):
    line = fin.readline().strip().split()

    nshy = int(line[0])

    totalshy = 0
    totalinvite = 0

    for j in xrange(0, nshy+1):
        currshy = int(line[1][j])
        if currshy == 0:
            continue
        if totalshy < j:
            toinvite = j-totalshy
            totalshy += toinvite
            totalinvite += toinvite
        totalshy += currshy

    result = totalinvite

    strout = "Case #" + str(i+1) + ": " + str(result) + "\n"
    #print strout
    fout.write(strout)
fin.close()
fout.close()
