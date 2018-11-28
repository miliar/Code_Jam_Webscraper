import sys

inp = open('B-large.in')
oup = open('B-large.out', 'w')
sys.stdout = oup

numCases = int(next(inp))

for case in range(numCases):
    print 'Case #' + str(case + 1) + ': ',
    dim = [int(x) for x in next(inp).split()]
    lawn = []
    for line in range(dim[0]):
        lawn.append([int(x) for x in next(inp)[:-1].split()])
    def check():
        for line in range(dim[0]):
            for grass in range(dim[1]):
                if lawn[line][grass] < max(lawn[line]):
                    if lawn[line][grass] != max(zip(*lawn)[grass]):
                        return False

        return True
    if check():
        print 'YES'
    else:
        print 'NO'
    
oup.close()
