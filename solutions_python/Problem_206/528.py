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
    d, n = [int(x) for x in next(it).strip().split()]
    horses = []
    for i in range(n):
        k, s = [int(x) for x in next(it).strip().split()]
        horses.append((k, s))

    hours_for_horses_to_arrive = [((d - k) / s) for (k, s) in horses]
    maximum_time = max(hours_for_horses_to_arrive)

    speed_to_travel = d / maximum_time

    answer = str(speed_to_travel)

    line = "Case #{0}: {1}\n".format(str(case), answer)
    output += line


with open(OUT_FILE, 'w') as fileOut:
    fileOut.write(output)
