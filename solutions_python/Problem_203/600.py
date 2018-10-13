def answer(dimension):
    row, column = int(dimension[0]), int(dimension[1])
    grid = [['' for _ in range(column)] for _ in range(row)]
    for i in range(row):
        grid[i] = list(input())
    occupied = {}
    empties = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '?':
                occupied[grid[i][j]] = [(i, j), (i, j)]
            else:
                empties.add((i, j))
    if len(empties) == 0:
        return grid

    for key in occupied:
        startX, startY = occupied[key][0]
        iteratorX = startX + 1
        while iteratorX != row and grid[iteratorX][startY] == '?':
            grid[iteratorX][startY] = key
            empties.remove((iteratorX, startY))
            iteratorX += 1
        occupied[key] = [(startX, startY), (iteratorX - 1, startY)]
    if len(empties) == 0:
        return grid
    for key in occupied:
        startX, startY = occupied[key][0]
        iteratorX = startX - 1
        while iteratorX != -1 and grid[iteratorX][startY] == '?':
            grid[iteratorX][startY] = key
            empties.remove((iteratorX, startY))
            iteratorX -= 1
        occupied[key] = [(iteratorX + 1, startY), occupied[key][1]]
    for key in occupied:
        startX, startY = occupied[key][0]
        lastX, lastY = occupied[key][1]
        iteratorY = startY + 1
        while iteratorY != column and\
                all(map(lambda x: grid[x][iteratorY] == '?', range(startX, lastX + 1))):
            for x in range(startX, lastX + 1):
                grid[x][iteratorY] = key
            iteratorY += 1
        occupied[key] = [(startX, startY), (lastX, iteratorY - 1)]
    for key in occupied:
        startX, startY = occupied[key][0]
        lastX, lastY = occupied[key][1]
        iteratorY = startY - 1
        while iteratorY != -1 and\
                all(map(lambda x: grid[x][iteratorY] == '?', range(startX, lastX + 1))):
            for x in range(startX, lastX + 1):
                grid[x][iteratorY] = key
            iteratorY -= 1
    return grid


def main():
    numCases = int(input())
    for i in range(numCases):
        inp = input().split(' ')
        result = answer(inp)
        print("Case #{}:".format(i + 1))
        for row in result:
            print("".join(row))


if __name__ == "__main__":
    main()
