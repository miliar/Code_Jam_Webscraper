import math

inputFile = open('A-small-attempt0.in', 'rb')

outputFile = open('A-small-attempt0.out', 'w')

T = int(inputFile.readline().rstrip("\n"))

for t in range(0, T):

    N = int(inputFile.readline().rstrip("\n"))

    # list to store all N strings
    strings = []
    min_strings = [] # removes duplicates
    min_string_chars = []

    for N in range(0, N):

        string = inputFile.readline().rstrip("\n")
        # append each string to our list
        strings.append(string)

        min_string_char = [0] # stores a count of each extra char
        min_string = string[0]

        for i in range(1, len(string)):
            if string[i] != min_string[-1]:
                min_string += (string[i])
                min_string_char.append(0)
            else:
                min_string_char[-1] += 1

        min_strings.append(min_string)
        min_string_chars.append(min_string_char)

    # go through each minified string to ensure they are equal
    win = True
    for ms in min_strings:
        if ms != min_strings[0]:
            win = False
            continue

    if not win:
        outputFile.write("Case #%d: %s\n" % (t+1, "Fegla Won"))
        continue

    changes = 0

    # for each character in the final string
    for i in range(0, len(min_string)):
        total = 0
        # for each array of counts
        for min_string_char in min_string_chars:
            total += min_string_char[i]
        average = int(round(total/len(min_string_chars)))
        for min_string_char in min_string_chars:
            changes += math.fabs(min_string_char[i] - average)

    outputFile.write("Case #%d: %d\n" % (t+1, (changes)))

inputFile.close()
outputFile.close()