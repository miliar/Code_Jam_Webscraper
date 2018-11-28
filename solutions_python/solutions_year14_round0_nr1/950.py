def loadWords():
    inFile = open('A-small-attempt0.in', 'r', 0)
    line = inFile.readlines()
    numLines = line.pop(0)
    line = [x.strip('\n') for x in line]
    temp = []
    for i in xrange(int(numLines)):
        temp.append(line[:10])
        line = line[10:]
    return temp, int(numLines)


def writeWords(lst):
    out = open('A-small-attempt0.out', 'w')
    count = 0
    for i in lst:
        count +=1
        out.write('Case #%d: ' %count + str(i) +'\n')
        
load, number = loadWords()
store = []
for row in load:
    first_row = int(row[0])
    second_row = int(row[5])
    test1 = row[first_row]
    test2 = row[second_row+5]
    test1 = test1.split(' ')
    test2 = test2.split(' ')
    test1 = [int(x) for x in test1]
    test2 = [int(x) for x in test2]
    test = list(set(test1) & set(test2))
    if len(test) == 1:
        store.append(test[0])
    elif len(test) > 1:
        store.append('Bad magician!')
    elif len(test) == 0:
        store.append('Volunteer cheated!')

writeWords(store)