fin = file("A-small-attempt0.in", "rU")
fout = file("A-small-attempt0.out", "w")

nruns = int(fin.readline().strip())
for i in xrange(nruns):
    rval = int(fin.readline().strip())

    nums = []

    for r in xrange(1, 5):
        line = fin.readline().strip().split()
        if r != rval:
            continue
        for c in xrange(4):
            nums.append(line[c])

    rval2 = int(fin.readline().strip())
    res = '0'
    dupe = False

    for r in xrange(1, 5):
        line = fin.readline().strip().split()
        if r != rval2:
            continue
        for c in xrange(4):
            if line[c] in nums:
                if res != '0':
                    dupe = True
                res = line[c]

    result = ''

    if dupe == True:
        result = "Bad magician!"
    elif res == '0':
        result = "Volunteer cheated!"
    else:
        result = res

    strout = "Case #" + str(i+1) + ": " + str(result) + "\n"
    #print strout
    fout.write(strout)
fin.close()
fout.close()
