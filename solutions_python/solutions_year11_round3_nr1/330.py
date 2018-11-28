__author__="ozgur"
__date__ ="$May 22, 2011 12:06:38 PM$"



def solve(tiles, Nc, Nr):
    for i in range(Nc):
        for j in range(Nr):
            if(tiles[i][j] == '#'):
                tiles[i][j] = '/'
                if(j+1 == Nr):
                    return 'Impossible'
                else:
                    if(tiles[i][j+1] == '.'):
                        return 'Impossible'
                    tiles[i][j+1] = '\\'
                if(i + 1 == Nc):
                    return 'Impossible'
                else:
                    if(tiles[i+1][j] == '.'):
                        return 'Impossible'
                    if(tiles[i+1][j+1] == '.'):
                        return 'Impossible'
                    tiles[i+1][j] = '\\'
                    tiles[i+1][j+1] = '/'

    return tiles

def handle():
    tiles = []
    solutions = []
    T = int(raw_input())
    for i in range(T):
        N = raw_input()
        Nc = int(N.split(' ')[0])
        Nr = int(N.split(' ')[1])
        for j in range(Nc):
            line = raw_input()
            lineList = []
            for e in line:
                lineList.append(e)
            tiles.append(lineList)
        solutions.append(solve(tiles, Nc, Nr))
        tiles = []

    for i in range(T):
        print 'Case #' + str(i+1) + ':'
        if 'I' in solutions[i]:
            print solutions[i]
        else:
            for line in solutions[i]:
                lineStr = ""
                for l in line:
                    lineStr  += l
                print lineStr



if __name__ == "__main__":
    handle()
