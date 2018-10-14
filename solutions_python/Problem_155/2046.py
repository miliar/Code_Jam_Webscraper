import os



def solveOvation(path):
    with open(path, "rt") as fin:
        stuff = fin.read().splitlines()
    string = ""
    for i in xrange(1, len(stuff)):

        peepnum = int(stuff[i].split()[0])
        shyness = stuff[i].split()[1]
        count = 0
        total = 0
        for j in xrange(peepnum+1):
            if total >= j:
                total += int(shyness[j])
            else:
                while total < j:
                    count+=1
                    total+=1
                total += int(shyness[j])
        string = string + "\nCase #%d: %d" %(i, count)
    with open("solution1 Large.txt", "wt") as fout:
        #string = "Case #%d: %d" %
        fout.write(string)
