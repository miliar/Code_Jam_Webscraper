import sys

def main():
    f = None
    output = None
    case = 1
    if len(sys.argv) > 1 :
        f = open(sys.argv[1])
        output = open(sys.argv[1][:-2] + 'out', 'w')
    else:
        print("PROBLEM")
        return
    tests = int(f.readline().strip())
    case = 1
    for t in range(tests):
        output.write("Case #" + str(case) + ": ")
        row1 = int(f.readline().strip())
        cards1 = []
        for n in range(4):
            line = f.readline()
            if n + 1 == row1:
                cards1 = line.strip().split()
        row2 = int(f.readline().strip())
        cards2 = []
        for n in range(4):
            line = f.readline()
            if n + 1 == row2:
                cards2 = line.strip().split()
        poss = 0
        card = ""
        #print("First row: " + str(cards1) + ", second row: " + str(cards2))
        for c in cards1:
            if c in cards2:
                poss += 1
                card = c
        if poss == 1:
            output.write(card + "\n")
        elif poss > 1:
            output.write("Bad magician!\n")
        else:
            output.write("Volunteer cheated!\n")
        case += 1

    f.close()
    output.close()

if len(sys.argv) > 1:
    main()
