import fileinput
input = fileinput.input()

cases = int(input.readline())
for c in range(cases):
    case = input.readline()
    case = case.split()[1]
    clapping = 0
    index = 0
    add = 0
    for char in case:
        char = int(char)
        if clapping < index:
            add += index - clapping
            clapping = index
        clapping += char
        index += 1
    print "Case #" + str(c + 1) + ": " + str(add)
