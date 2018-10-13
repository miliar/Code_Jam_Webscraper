def findDown(y, x, alMap):
    minimum = alMap[y][x]
    direct = ''
    
    try:
        if y != 0 and alMap[y-1][x] < alMap[y][x]:
            minimum = alMap[y-1][x]
            direct = 'N'
    except IndexError:
        pass

    try:
        if x != 0 and alMap[y][x-1] < minimum:
            minimum = alMap[y][x-1]
            direct = 'W'
    except IndexError:
        pass
    
    try:
        if alMap[y][x+1] < minimum:
            minimum = alMap[y][x+1]
            direct = 'E'
    except IndexError:
        pass
    
    try:
        if alMap[y+1][x] < minimum:
            minimum = alMap[y+1][x]
            direct = 'S'
    except IndexError:
        pass

    return direct

def initFlow(y, x, label, alMap, result):
    stack = []

    while 1:
        stack.append((y,x))
        direct = findDown(y, x, alMap)

        if direct == '':
            break

        if direct == 'N':
            y = y - 1
        elif direct == 'W':
            x = x - 1
        elif direct == 'E':
            x = x + 1
        else:
            y = y + 1

        if result[y][x] != '':
            for cord in stack:
                result[cord[0]][cord[1]] = result[y][x]

            return label

    for cord in stack:
        result[cord[0]][cord[1]] = label

    return chr(ord(label)+1)
    
def initMap(f, height):
    alMap = []
    
    for y in range(height):
        alMap.append([int(x) for x in f.readline().split()])

    return alMap
    
def main():
    
    f = open('B-large.in')
    outf = open('b-result.txt','w')

    nMap = int(f.readline())

    case = 1
    for x in range(nMap):
        
        height, width = map(lambda x: int(x), f.readline().split())

        alMap = initMap(f, height)
        result = [[ '' for y in range(width) ] for x in range(height) ]

        nowLabel = 'a'

        for yy in range(height):
            for xx in range(width):
                if result[yy][xx] == '':
                    nowLabel = initFlow(yy, xx, nowLabel, alMap, result)

        outf.write('Case #')
        outf.write(str(case))
        outf.write(':\n')
        case = case+1

        for row in result:
            for l in row:
                outf.write(l+' ')
            outf.write('\n')
    f.close()
    outf.close()
    
main()
