__author__ = 'sean223'


# IN_FILE = 'test_input.txt'
# OUT_FILE = 'test_output.txt'

# IN_FILE = 'A-small.in'
# OUT_FILE = 'small_out.txt'

IN_FILE = 'A-large.in'
OUT_FILE = 'large_out.txt'


with open(IN_FILE, 'r') as fileIn:
    fileLines = fileIn.readlines()

it = iter(fileLines)
numbCases = int(next(it))
output = ""


for case in range(1, numbCases+1):
    input_line = next(it).strip().split(' ')
    pancakes = [x == '+' for x in input_line[0]]
    k = int(input_line[1])
    number_flips = 0

    for i in range(0, len(pancakes)-k+1):
        if not pancakes[i]:
            number_flips += 1
            for j in range(k):
                pancakes[i+j] = not pancakes[i+j]

    if not all(pancakes):
        number_flips = 'IMPOSSIBLE'

    line = "Case #{0}: {1}\n".format(str(case), str(number_flips))
    output += line


with open(OUT_FILE, 'w') as fileOut:
    fileOut.write(output)
