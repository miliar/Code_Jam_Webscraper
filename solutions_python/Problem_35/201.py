T = int(raw_input().strip())

def basin(letter, x, y):
    global heightmap, basinmap

    if (x, y) in basinmap:
        return basinmap[x, y]

    width = len(heightmap[y]) #uniform width
    height = len(heightmap)

    neighbours = []
    for delta in range(-1, 2, 2):
        for coord in range(2):
            if (coord and not delta == -1) or (delta == -1 and not coord):
                if (0 <= (y + delta) < height):
                    neighbours.append((x, y + delta, heightmap[y + delta][x]))
                else:
                    neighbours.append((x, y + delta, 10001))
            else:
                if (0 <= (x + delta) < width):
                    neighbours.append((x + delta, y, heightmap[y][x + delta]))
                else:
                    neighbours.append((x + delta, y, 10001))

    destineighbour = min(neighbours, key=lambda neighbour: neighbour[2])
    if destineighbour[2] >= heightmap[y][x]:
        #We're a sink
        basinmap[x,y] = letter
        return letter
    else:
        basinmap[x,y] = basin(letter, *destineighbour[:2])
        return basinmap[x,y]
        


for x in range(T):
    print 'Case #%s:' % (x + 1)
    h, w = map(int, raw_input().strip().split())
    heightmap = []

    for hi in range(h):
        heightmap.append(map(int, raw_input().strip().split()))

    basinmap = {}
    guess = 97 #lowercase a
    for y in range(h):
        for x in range(w):
            ans = basin(chr(guess), x, y)
            if ans == chr(guess):
                #The letter was used
                guess += 1

    for y in range(h):
        for x in range(w):
            print basinmap[x, y],
        print
    
        
        
