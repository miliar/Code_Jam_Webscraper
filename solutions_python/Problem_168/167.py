__author__ = 'sean'


# IN_FILE = 'stress_test.txt'
# OUT_FILE = 'stress_test_out.txt'

# IN_FILE = 'A-small.in'
# OUT_FILE = 'A-small_out.txt'

IN_FILE = 'A-large.in'
OUT_FILE = 'A-large_out.txt'


with open(IN_FILE, 'r') as fileIn:
    fileLines = fileIn.readlines()

it = iter(fileLines)
numbCases = int(next(it))
output = ""


for case in range(numbCases):
    line = next(it).rstrip().split()
    r, c = int(line[0]), int(line[1])
    grid = []
    for _i in range(r):
        grid.append(next(it).rstrip())

    swaps = 0
    possible = True
    row, col = 0, 0
    while True:
        character = grid[row][col]
        if character == '.':
            pass
        else:
            above, right, below, left = False, False, False, False
            for higher_row in range(0, row):
                if grid[higher_row][col] != '.':
                    above = True
                    break
            for lower_row in range(row+1, r):
                if grid[lower_row][col] != '.':
                    below = True
                    break
            for lefter_col in range(0, col):
                if grid[row][lefter_col] != '.':
                    left = True
                    break
            for righter_col in range(col+1, c):
                if grid[row][righter_col] != '.':
                    right = True
                    break

            possible = above or right or below or left
            if not possible:
                answer = 'IMPOSSIBLE'
                break

            elif character == '>' and right:
                pass
            elif character == '<' and left:
                pass
            elif character == 'v' and below:
                pass
            elif character == '^' and above:
                pass
            else:
                swaps += 1

        col += 1
        if col >= c:
            col = 0
            row += 1
            if row >= r:
                break

    if possible:
        answer = str(swaps)

    line = "Case #{0}: {1}\n".format(str(case+1), str(answer))
    output += line


with open(OUT_FILE, 'w') as fileOut:
    fileOut.write(output)
