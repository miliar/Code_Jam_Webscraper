def recurse(grid, index, size, flips):
    if '-' not in grid:
        return flips
    if index == len(grid) - size + 1:
        return float('inf')
    flippedGrid = grid[:]
    for n in range(index, index+size):
        if flippedGrid[n] == '+':
            flippedGrid[n] = '-'
        else:
            flippedGrid[n] = '+'
    return min(recurse(grid, index+1, size, flips), recurse(flippedGrid, index+1, size, flips+1))

def main():
    f1 = open('in.txt', 'r')
    f2 = open('out.txt', 'w')
    t = int(f1.readline())
    for n in range(0, t):
        header = 'Case #' + str(n+1) + ': '
        data = f1.readline().split(' ')
        grid = list(data[0])
        k = int(data[1])
        output = recurse(grid, 0, k, 0)
        if output == float('inf'):
            output = 'IMPOSSIBLE'
        else:
            output = str(output)
        f2.write(header + output + '\n')
main()