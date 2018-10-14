

def isPossible(pattern):
    patternCopy = []
    for row in pattern:
        maxV = max(row)
        patternCopy.append([maxV for i in range(0, len(row))])

    col = 0
    totalCols = len(pattern[0])
    while col < totalCols:
        patternCopyCol = [r[col] for r in patternCopy]
        patternCol = [r[col] for r in pattern]
        if patternCopyCol != patternCol:
            minV = min(patternCol)
            for e in patternCol:
                if e != minV:
                    return 'NO'
        col += 1
    return 'YES'



def jamout(filename, outputs):
    fout = open(filename, 'wt')
    for i, output in enumerate(outputs):
        fout.write('Case #' + str(i + 1) + ': ' + output + "\n")
    fout.close()



filename = 'B-small-attempt4.in'
datasets = []
with open(filename, 'rt') as f:
    testCases = int(next(f))
    while 0 < testCases:
        dim = [int(e) for e in next(f).rstrip().split()]
        dataset = []
        for i in range(0, dim[0]):
            dataset.append([int(e) for e in next(f).rstrip().split()]);
        datasets.append(dataset)
        testCases -= 1



outputs = []
for key, dataset in enumerate(datasets):
    #print("key: ", key)
    outputs.append(isPossible(dataset))
jamout('B-small-attempt4.txt', outputs)
#print(outputs)

        
