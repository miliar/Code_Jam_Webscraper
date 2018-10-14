'''
Google Code Jam 2009
Qualification Round
B. Watersheds

@author: Samuel Spiza
'''

def fillKeyMap(map, keyMap):
    letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    i = 0
    maxY, maxX = len(map), len(map[0])
    for y in range(maxY):
        for x in range(maxX):
            recursive(y, x, map, keyMap, letter)

def recursive(y, x, map, keyMap, letter):
    if keyMap[y][x] != "":
        return keyMap[y][x]
    maxY, maxX = len(map), len(map[0])
    a = 100000
    tempArray = [a for z in range(4)]
    indices = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    for i in range(4):
        yNow, xNow = y + indices[i][0], x + indices[i][1]
        if 0 <= yNow and 0 <= xNow and xNow < maxX and yNow < maxY and map[yNow][xNow] < map[y][x]:
            tempArray[i] = map[yNow][xNow]
    if 4*a == sum(tempArray):
        keyMap[y][x] = letter.pop(0)
    else:
        j = tempArray.index(min(tempArray))
        keyMap[y][x] = recursive(y + indices[j][0], x + indices[j][1], map, keyMap, letter)
    return keyMap[y][x]

            
#fileName = "B-small-practice.in"
#fileName = "B-small-attempt0.in"
fileName = "B-large.in"
file = open(fileName, "r")

maps = []
keyMaps = []
i = -1

for line in file:
    if i == -1:
        T = int(line.strip())
        i = 1
    elif i == 0:
        tempArray = line.strip().split()
        H = int(tempArray[0])
        W = int(tempArray[1])
        maps.append([])
        keyMaps.append([])
        i = H + 1
    elif 0 < i:
        maps[-1].append([int(x) for x in line.strip().split()])
        keyMaps[-1].append(["" for x in line.strip().split()])
    i = i - 1

file.close()
    
#print maps

string = ""
for t in range(T):
    fillKeyMap(maps[t], keyMaps[t])
    string = string + "Case #" + str(t + 1) + ":\n"
    for line in keyMaps[t]:
        string = string + " ".join(line) + "\n"
        
file = open(fileName.rsplit(".", 1)[0] + ".out", "w")
file.write(string.strip())
file.close()
