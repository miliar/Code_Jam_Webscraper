import sys


def readint():
    return int(sys.stdin.readline().strip())

def readgrid():
    grid = []
    for i in range(4):
        grid.append([int(x) for x in sys.stdin.readline().strip().split()])
    return grid



def main():
    test_cases = readint()

    for i in range(1, test_cases+1):
        row1 = readint() - 1
        grid1 = readgrid()
        row2 = readint() - 1
        grid2 = readgrid()
        answers = {el for el in grid1[row1]} & {el for el in grid2[row2]}

        if len(answers) == 0:
            result = "Volunteer cheated!"
        elif len(answers) == 1:
            result = str(list(answers)[0])
        else:
            result = "Bad magician!"
        print "Case #%d: %s" % (i, result,)


if __name__ == "__main__":
    main()
