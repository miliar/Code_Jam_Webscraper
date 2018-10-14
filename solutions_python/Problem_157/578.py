def main():
    file = open('C-small-attempt1.in', 'r')
    cases = int(file.readline())
    for x in range(cases):
        line = lineToIntList(file.readline())
        # print(line)
        input = file.readline().strip()
        answer = solve(input, line[0], line[1])
        output = "Case #" + str(x+1) + ": " + str(answer)
        print(output)


def solve(input, length, iterations):
    newstring = input[:] * iterations
    # print(newstring)
    iFound = False
    jFound = False
    kFound = False
    negative = False
    if newstring == 'ijk':
        return 'YES'
    while len(newstring) > 1:
        # print(newstring)
        reduction = newstring[0:2]
        # print(reduction)
        out = red(reduction)
        # print(out)
        suffix = newstring[2:]
        # print(suffix)
        # print(out)
        if negative and out[:1] == '-':
            negative = False
            out = out[1:]
        elif out[:1] == '-':
            negative = True
            out = out[1:]
        newstring = out + suffix
        if newstring[:1] == 'i' and not iFound:
            # print("I found")
            iFound = True
            newstring = newstring[1:]
        if iFound and newstring[:1] == 'j' and not jFound:
            # print("J found")
            jFound = True
            newstring = newstring[1:]
        if jFound and newstring == 'k':
            # print("K found")
            kFound = True
        if kFound and negative is False:
            return "YES"
    else:
        return "NO"


def red(input):
    if input == "ii":
        return "-"
    if input == "ij":
        return "k"
    if input == "ik":
        return "-j"
    if input == "ji":
        return "-k"
    if input == "jj":
        return "-"
    if input == "jk":
        return "i"
    if input == "ki":
        return "j"
    if input == "kj":
        return "-i"
    if input == "kk":
        return "-"


def lineToIntList(line):
    return map(int, line.strip().split())


def lineToList(line):
    return line.strip().split()

if __name__ == '__main__':
    main()
