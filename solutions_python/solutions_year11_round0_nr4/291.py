
def findHits(seq):
    ''' find the size of all of the closed groups of seq[x] = y, seq[y] = x, etc '''
    used = set()
    total = 0
    for i in range(0, len(seq)):
        # if this index hasn't been used yet, and is in the wrong spot
        if seq[i] != i and i not in used:
            head = i
            next = seq[i]
            used.add(next)
            hits = 1
            while  next != head:
                hits += 1
                next = seq[next]
                used.add(next)
            total += hits
    return total



fin = open("large.in", "r")
fout = open("large.out", "w")

line = fin.readline()

numCases = int(line)
curCase = 1
while curCase <= numCases:
    line = fin.readline()
    line = fin.readline()
    elements = line.split()
    
    seq = []
    for i in elements:
        seq.append(int(i)-1)
        
    hits = findHits(seq)
    
    fout.write("Case #" + str(curCase) + ": " + str(hits) + "\n")
    
    curCase += 1

fin.close()
fout.close()
        

