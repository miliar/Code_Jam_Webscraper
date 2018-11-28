__author__ = 'sean223'


# IN_FILE = 'test_input.txt'
# OUT_FILE = 'test_output.txt'

IN_FILE = 'B-small.in'
OUT_FILE = 'small_out.txt'

# IN_FILE = 'B-large.in'
# OUT_FILE = 'large_out.txt'


with open(IN_FILE, 'r') as fileIn:
    fileLines = fileIn.readlines()

it = iter(fileLines)
numbCases = int(next(it))
output = ""


def place_primary(stables, primary_color, amount):
    index = 0
    number_to_place = amount
    modulus = len(stables)
    while number_to_place > 0:
        attempts = 0
        while not stables[index] == '' or stables[(index-1) % modulus] == primary_color or stables[(index+1) % modulus] == primary_color:
            attempts += 1
            if attempts > 2*modulus:
                return stables, False
            index = (index + 1) % modulus

        stables[index] = primary_color
        number_to_place -= 1
        if number_to_place == 0:
            break

        attempts = 0
        while not stables[index] == '':
            attempts += 1
            if attempts > 2 * modulus:
                return stables, False
            index = (index + 1) % modulus

        index = (index + 1) % modulus

    return stables, True


for case in range(1, numbCases+1):
    n, r, o, y, g, b, v = [int(x) for x in next(it).strip().split()]
    answer = ['' for _i in range(n)]

    primaries = [(r, 'R'), (y, 'Y'), (b, 'B')]
    primaries.sort(reverse=True)
    for color in primaries:
        if color[0] > 0:
            answer, success = place_primary(answer, color[1], color[0])
            if not success:
                answer = 'IMPOSSIBLE'
                break

    line = "Case #{0}: {1}\n".format(str(case), ''.join(answer))
    output += line


with open(OUT_FILE, 'w') as fileOut:
    fileOut.write(output)
