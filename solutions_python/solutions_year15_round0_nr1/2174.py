import fileinput

with fileinput.input() as f:
    f.readline()
    case = 1
    for line in f:
        line = line[:-1]
        tokens = line.split()
        smax = int(tokens[0])
        s = 0
        people = 0
        needed = 0
        for c in tokens[1]:
            if people < s:
                needed += s - people
                people = s
            people += int(c)
            s += 1
        print("Case #{}: {}".format(case, needed))
        case += 1
