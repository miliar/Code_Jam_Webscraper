def main():
    input = open('A-large.in', 'r')
    numCases = int(input.readline().strip())

    case = 0

    for line in input:
        case = case + 1
        cakes, k = line.strip().split()
        calcPancakes(list(cakes), int(k), case)


def calcPancakes(cakes, k, case):

    flips = 0

    while not isDone(cakes):

        firstBlank = cakes.index("-")

        if (len(cakes) < firstBlank + k):
            print "Case #{0}: IMPOSSIBLE".format(case)
            return

        cakes = flip(cakes, firstBlank, k)

        flips = flips + 1
        continue

    print "Case #{0}: {1}".format(case, flips)
    return

def isDone(cakes):
    return all([x == "+" for x in cakes])

def flip(cakes, n, k):
    for x in range(n, n+k):
        if cakes[x] == "+":
            cakes[x] = "-"
        else:
            cakes[x] = "+"
    return cakes

if __name__ == '__main__':
    main()