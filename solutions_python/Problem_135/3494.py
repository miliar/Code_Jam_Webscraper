__author__ = 'iraasta'


def start():
    t = range(int(raw_input()))
    for a in t:
        run(a+1)


def run(case):
    row1 = int(raw_input())-1

    l = range(4)
    lines1 = []
    for i in l:
        lines1.append(raw_input().split(" "))

    row2 = int(raw_input())-1
    lines2 = []
    for i in l:
        lines2.append(raw_input().split(" "))

    chosennum = []
    chosenlines = [lines1[row1], lines2[row2]]
    for a in chosenlines[0]:
        for b in chosenlines[1]:
            if b == a:
                chosennum.append(a)

    if len(chosennum) == 0:
        print "Case #{0}: {1}".format(case, "Volunteer cheated!")
    elif len(chosennum) == 1:
        print "Case #{0}: {1}".format(case, chosennum[0])
    else:
        print "Case #{0}: {1}".format(case, "Bad magician!")


if __name__ == "__main__":
    start()