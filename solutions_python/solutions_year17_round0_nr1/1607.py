import fileinput

def side(cake):
    if cake == "+":
        return 0
    else:
        return 1

def parse(line):
    tokens = line.split()
    cakes = [side(cake) for cake in tokens[0]]
    k = int(tokens[1])
    return cakes, k

def find_flips(line):
    cakes, k = parse(line)
    ends = [0 for c in cakes]
    total = 0
    currect = 0
    for i in range(len(cakes)):
        cake = cakes[i]
        currect -= ends[i]
        if (cake + currect) % 2 == 1:
            if i + k > len(cakes):
                return "IMPOSSIBLE"
            if i + k < len(cakes):
                ends[i + k] += 1
            total += 1
            currect += 1
    return str(total)

def main():
    file = fileinput.input()
    n = int(file.readline())
    for i in range (1, n + 1):
        line = file.readline()
        flips = find_flips(line)
        print "Case #%d: %s" % (i, flips)


if __name__ == "__main__":
    main()
