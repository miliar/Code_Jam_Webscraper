__author__ = 'nguyensontung1404'

if __name__ == "__main__":
    import sys
    sys.stdin = open("A-small-attempt0.in")
    sys.stdout = open("output.txt", "w")
    for case in range(1, int(sys.stdin.readline())+1):
        index1 = int(sys.stdin.readline())-1
        for i in range(4):
            _str = sys.stdin.readline()
            if i == index1:
                first = map(int, _str.split(" "))
        index2 = int(sys.stdin.readline())-1
        for i in range(4):
            _str = sys.stdin.readline()
            if i == index2:
                second = map(int, _str.split(" "))
        result = list(set(first) & set(second))
        if len(result) == 1:
            print "Case #%d: %d" % (case, result[0])
        elif len(result) == 0:
            print "Case #%d: Volunteer cheated!" % case
        else:
            print "Case #%d: Bad magician!" % case
