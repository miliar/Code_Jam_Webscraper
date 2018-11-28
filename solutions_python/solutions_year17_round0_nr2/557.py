__author__ = 'sean223'


# IN_FILE = 'test_input.txt'
# OUT_FILE = 'test_output.txt'

# IN_FILE = 'B-small.in'
# OUT_FILE = 'small_out.txt'

IN_FILE = 'B-large.in'
OUT_FILE = 'large_out.txt'


with open(IN_FILE, 'r') as fileIn:
    fileLines = fileIn.readlines()

it = iter(fileLines)
numbCases = int(next(it))
output = ""


for case in range(1, numbCases+1):
    n_string = next(it).strip()
    n = int(n_string)

    i = 0
    while i < len(n_string)-1:
        if int(n_string[len(n_string) - i - 1]) < int(n_string[len(n_string) - i - 2]):
            n = ((n - 10**(i+1)) // 10**(i+1)) * 10**(i+1) + 10**(i+1) - 1
            n_string = str(n)
        i += 1

    line = "Case #{0}: {1}\n".format(str(case), n_string)
    output += line


with open(OUT_FILE, 'w') as fileOut:
    fileOut.write(output)
