def compare(actual, mine):
    for i in range(0, len(actual)):
        for j in range(0, len(actual[i])):
            if actual[i][j] != mine[i][j]:
                return "NO"

    return "YES"

def findHeighst(row):
    heighest = 0
    for h in row:
        if h > heighest:
            heighest = h

    return heighest

i = open('B-large.in', 'r+')
o = open('output.txt', 'w+')

text = i.readlines()

num = int(text[0])
del[text[0]]

for k in range(0, num):
    temp = text[0].split(' ')
    n = int(temp[0])
    m = int(temp[1])
    del[text[0]]

    startingLawn = []
    lawnAfter = []

    # Initilize starting array
    for i in range(0, n):
        startingLawn.append([])
        for j in range(0, m):
            startingLawn[i].append(100)

    # Initilize lawn after array
    for i in range(0, n):
        lawnAfter.append([])
        temp = text[0].split(' ')
        del[text[0]]
        for j in range(0, m):
            lawnAfter[i].append(int(temp[j]))


    # Cut Rows
    for i in range(0, n):
        heighest = findHeighst(lawnAfter[i])
        for j in range(0, m):
            startingLawn[i][j] = heighest

    # Cut Columns
    for i in range(0, m):
        # Convert col to row
        row = []
        for j in range(0, n):
            row.append(lawnAfter[j][i])        
        heighest = findHeighst(row)
        ##
                       
        for j in range(0, n):
            if startingLawn[j][i] > heighest:
                startingLawn[j][i] = heighest



    # Compare the cut lawn to what it should be
    result = compare(lawnAfter, startingLawn)

    o.write("Case #" + str(k+1) + ": " + result + "\n")

o.close()
print('DONE')
        

            
