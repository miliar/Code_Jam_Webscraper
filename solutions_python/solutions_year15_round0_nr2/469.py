f = open('B-large.in', 'r')
g = open('output2.txt', 'w')

num = int(f.readline())
for i in range (num):
    numDiners = int(f.readline())
    data = f.readline().split()
    highest = 0
    for pos in range(numDiners):
        data[pos] = int(data[pos])
        if data[pos] > highest:
            highest = data[pos]
    minTime = highest
    top = 1
    while top < minTime:
        splits = 0
        localMax = 0
        for diner in data:
            addSplits = (diner-1)//top
            new = (diner-1)//(addSplits+1) + 1
            if new > localMax:
                localMax = new
            splits += addSplits
        time = splits + localMax
        if time < minTime:
            minTime = time
        top += 1

    s = "Case #" + str(i+1) + ": " + str(minTime) + '\n'
    g.write(s)

f.close()
g.close()


