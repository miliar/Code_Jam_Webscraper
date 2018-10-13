from string import *

def read_words(filename):
    '''
    converts a file to a list
    '''
    
    words = []
    for line in filename:
            words.append(line.strip())
    return words

filename = open("coddy.txt", 'r')
inputfile = read_words(filename)

numcases = int(inputfile[0])

for i in range (numcases):
    rownums = []
    grid1 = []
    grid2 = []
    rownums[0:1] = (int(inputfile[1+(10*i)]), int(inputfile[6+(10*i)]))

    for j in range(4):
        grid1 += inputfile[(2+(10*i)+j)].split()
        grid2 += inputfile[(7+(10*i)+j)].split()
    for element in range (16):
        grid1[element] = int(grid1[element])
        grid2[element] = int(grid2[element])

    startrow = grid1[4*(rownums[0]-1) : 4*(rownums[0]-1) + 4]
    endrow = grid2[4*(rownums[1]-1) : 4*(rownums[1]-1) + 4]
    
    wins = []
    for k in range(4):
        for l in range(4):
            e1 = startrow[k]
            e2 = endrow[l]

            if (e1 == e2):
                wins.append(e1)
                
    result = ""
    result+= "Case #" + str(i+1) + ": "
    if (len(wins) == 1):
        result+=  str(wins[0])
    elif (len(wins)>1):
        result+= "Bad magician!"
    else:
        result+= "Volunteer cheated!"
    print result
    