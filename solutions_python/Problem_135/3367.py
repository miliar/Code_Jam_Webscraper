import sys

def main(filename):
    r = open(filename, 'r')
    r.readline() #ignore the number input
    w = open("p1out.txt", "w")
    count = 1
    while True:
        line1 = r.readline()
        if line1 == "":
            break
        a1 = int(line1) - 1
        lines = []
        for x in range(4):
            lines.append([int(n) for n in r.readline().split(" ")])
        row1 = lines[a1]


        print "-------"
        print row1


        lines = []
        a2 = int(r.readline()) -1
        for x in range(4):
            lines.append([int(n) for n in r.readline().split(" ")])
        row2 = lines[a2]

        print row2

        possible = [x for x in row1 if x in row2]
        outLine = "Case #" + str(count) + ": "

        print possible

        if len(possible) == 0:
            outLine += "Volunteer cheated!"
        elif len(possible) ==1:
            outLine += str(possible[0])
        else:
            outLine += "Bad magician!"
        outLine += "\n"
        w.write(outLine)
        count += 1

    r.close()
    w.close()


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)
