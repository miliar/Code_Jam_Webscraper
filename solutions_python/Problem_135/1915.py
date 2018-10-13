with open('A-small-attempt0.in', 'r') as f, open('A-small-attempt0.out', 'w') as out:
    samples = int(f.readline())
    for testN in range(samples):
        firstChoice = int(f.readline()) - 1    # zero indexing
        firstArrange = []
        for i in range(4):
            firstArrange.append(set([int(x) for x in f.readline().split()]))
        
        secondChoice = int(f.readline()) - 1    # zero indexing
        secondArrange = []
        for i in range(4):
            secondArrange.append(set([int(x) for x in f.readline().split()]))

        overlap = firstArrange[firstChoice] & secondArrange[secondChoice]

        
        if len(overlap) == 1:
            output = str(list(overlap)[0])
        elif len(overlap) > 1:
            output = "Bad magician!"
        else:
            output = "Volunteer cheated!"
            
        out.write("Case #%d: %s\n" % (testN+1, output))
        
