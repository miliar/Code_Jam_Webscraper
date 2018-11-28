def pancakeFlipper(pancakes, flipperSize, tc, outFile):
    pancakes = list(pancakes)
    if len(pancakes) == 1 and pancakes == "+":
        print("Case #" + str(tc) + ": 0", file = outFile)
    elif len(pancakes) == 1 and pancakes == "-" and flipperSize == 1:
        print("Case #" + str(tc) + ": 1", file = outFile)
    elif len(pancakes) < flipperSize:
        print("Case #" + str(tc) + ": IMPOSSIBLE", file = outFile)
    elif len(pancakes) == flipperSize:
        happy, sad = 0, 0
        for pk in pancakes:
            if pk == "+":
                happy += 1
            else:
                sad += 1
        if happy == flipperSize:
            print("Case #" + str(tc) + ": 0", file = outFile)
        elif sad == flipperSize:
            print("Case #" + str(tc) + ": 1", file = outFile)
        else:
            print("Case #" + str(tc) + ": IMPOSSIBLE", file = outFile)
    else:
        flips = 0
        length = len(pancakes)
        index = 0
        while index <= length - flipperSize:
            if pancakes[index] == '-':
                tempIndex = index
                counter = 0
                while tempIndex < length and counter < flipperSize:
                    if pancakes[tempIndex] == '+':
                        pancakes[tempIndex] = '-'
                    else:
                        pancakes[tempIndex] = '+'
                    counter += 1
                    tempIndex += 1
                flips += 1
            else:
                index += 1

        impossible = False
        for pk in pancakes:
            if pk == '-':
                impossible = True
                break

        if not impossible:
            print("Case #" + str(tc) + ": " + str(flips), file = outFile)
        else:
            print("Case #" + str(tc) + ": IMPOSSIBLE", file = outFile)


def main():
    inFile = open('sample.txt', 'r')
    outFile = open('output.txt', 'w')
    for line in inFile:
        tc = int(line)
        break
    count = 1
    for line in inFile:
        line = line.strip().split()
        pancakes = line[0].strip()
        flipperSize = int(line[1].strip())
        pancakeFlipper(pancakes, flipperSize, count, outFile)
        count += 1

if __name__ == '__main__':
    main()

