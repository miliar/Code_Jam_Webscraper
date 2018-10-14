# magictrick.py
# Google Code Jam 2014
# Chad Gibbons, dcgibbons@gmail.com

import fileinput

file_input = fileinput.input()
T = int(file_input.readline())

def read_set(file_input):
    answer = int(file_input.readline())
    grid = 4 * [None]
    for i in range(0, 4):
        row = file_input.readline().rstrip().split(' ')
        grid[i] = [int(x) for x in row]
    return answer,grid


for test_case in range(1, T+1):
    answer1,grid1 = read_set(file_input)
    answer2,grid2 = read_set(file_input)

    matches = 0
    match_card = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if grid1[answer1-1][i] == grid2[answer2-1][j]:
                matches += 1
                match_card = grid1[answer1-1][i]
    if matches == 1:
        print "Case #%d: %d" % (test_case, match_card)
    elif matches == 0:
        print "Case #%d: Volunteer cheated!" % (test_case)
    else:
        print "Case #%d: Bad magician!" % (test_case)
