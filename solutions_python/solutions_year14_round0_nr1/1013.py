import sys


def main(sys.argv):
    print(argv[0])
    f = open(sys.argv[0], 'r')
    out = open('out.txt', 'w')
    cases = int(f.readline())
    for i in range(cases):
        ans1 = int(f.readline())
        grid1 = []
        for j in range(4):
            grid1.append([int(x) for x in f.readline().split()])
        ans2 = int(f.readline())
        grid2 = []
        for j in range(4):
            grid2.append([int(x) for x in f.readline().split()])
            result = ""
        intersection = list(set(grid1[ans1 - 1]).intersection(grid2[ans2 - 1]))
        s = len(intersection)
        if s == 1:
            result = str(intersection[0])
        elif s == 0:
            result = 'Volunteer cheated!'
        else:
            result = 'Bad magician!'
        out.write('Case #' + str(i + 1) + ': ' + result + '\n')


if __name__ == 'main':
    main(sys.argv)
