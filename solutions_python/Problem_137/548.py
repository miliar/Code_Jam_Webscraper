data = open('minesweeper.txt')

mines = {}

while True:
    line = data.readline()
    line = line.split()
    if len(line) == 0:
        break
    R = int(line[0])
    C = int(line[1])
    M = int(line[2])
    line = data.readline().strip()
    if line == 'Impossible':
        mines[(R, C, M)] = 'Impossible'
    else:
        mine = line + '\n'
        for r in range(1, R):
            mine += data.readline()
        mines[(R, C, M)] = mine

test_data = open('C-small-attempt0.in')
num_tests = int(test_data.readline().strip())
for test in range(num_tests):
    line = test_data.readline().split()
    R = int(line[0])
    C = int(line[1])
    M = int(line[2])
    output = mines[(R, C, M)]
    print('Case #{0}:'.format(test + 1))
    print(output)
