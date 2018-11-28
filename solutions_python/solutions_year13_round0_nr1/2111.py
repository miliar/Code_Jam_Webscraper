#############
# Google Code Jam 2013
# by Jos Kraaijeveld
# @JMKraaijeveld
# kaidence.org
#############
import sys


def find_winner(field):
    finished = True
    # Horizontal check
    for line in field:
        if line.count('X') == 4 or (line.count('X') == 3 and 'T' in line):
            return 'X won'
        if line.count('O') == 4 or (line.count('O') == 3 and 'T' in line):
            return 'O won'
        if '.' in line:
            finished = False
    # Vertical check
    for i in range(0, 4):
        line = [x[i] for x in field]
        if line.count('X') == 4 or (line.count('X') == 3 and 'T' in line):
            return 'X won'
        if line.count('O') == 4 or (line.count('O') == 3 and 'T' in line):
            return 'O won'
    # Diagonal check
    line = [field[i][i] for i in range(0, len(field))]
    if line.count('X') == 4 or (line.count('X') == 3 and 'T' in line):
        return 'X won'
    if line.count('O') == 4 or (line.count('O') == 3 and 'T' in line):
        return 'O won'
    line = [field[3-i][i] for i in range(3, -1, -1)]
    if line.count('X') == 4 or (line.count('X') == 3 and 'T' in line):
        return 'X won'
    if line.count('O') == 4 or (line.count('O') == 3 and 'T' in line):
        return 'O won'
    # Draw check
    if finished:
        return 'Draw'
    else:
        return 'Game has not completed'

 
# Open the files and read the arguments
input = open(sys.argv[1])
output = open(sys.argv[2], 'w')
num_cases = int(input.readline())
current = 1

# Loop over the amount of testcases
while current <= num_cases:
    field = []
    line = input.readline()[:-1]
    while line:
        field.append(line)
        line = input.readline()[:-1]
    output.write("Case #{}: {}\n".format(current, find_winner(field)))
    current += 1

input.close()
output.close()
 
