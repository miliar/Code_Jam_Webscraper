# codejam fair and square

from math import sqrt

ifl = open('C-small-attempt0.in')
infile = ifl.readlines()

# for each range
# check if number is palindrome
    # if true, check if sqrt is also palindrome

numCases = int(infile[0])
i = 1

while i <= numCases:  # until we reach end of file
    line = infile[i].split(' ')
    low = int(line[0])
    high = int(line[1])

    results = 0

# okay maybe

    for integer in range(low, high + 1):
        if (str(integer) == str(integer)[::-1]):
            tmp = sqrt(integer)
            root = str(tmp)[:-2]
            if root == root[::-1] or root == 2:
                results = results + 1

    newline = "Case #" + str(i) + ": " + str(results) + "\n"
    outfile = open('c.out','a+b').write(newline)

    i = i + 1