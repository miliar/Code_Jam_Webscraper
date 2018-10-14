
__author__ = 'shokoufeh'


import sys

if __name__ == "__main__":
    fp = open("A1.in")
    sys.stdout = open("A1.out", "w")

    Test = int(fp.readline())
    for t in range(Test):
        javab = 0

        Line = fp.readline()
        S = int(Line.split()[0])
        Sum = 0

        for i, c in enumerate(Line.split()[1]):
            if Sum < i and int(c) > 0:
                javab += i - Sum
                Sum = i

            Sum += int(c)

        print "Case #%s: %s" % (t + 1, javab)


