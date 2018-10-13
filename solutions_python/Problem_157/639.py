__author__ = 'amolina'


MULT = {
    ("1", "1"): "1",
    ("1", "-1"): "-1",
    ("1", "i"): "i",
    ("1", "-i"): "-i",
    ("1", "j"): "j",
    ("1", "-j"): "-j",
    ("1", "k"): "k",
    ("1", "-k"): "-k",

    ("-1", "1"): "-1",
    ("-1", "-1"): "1",
    ("-1", "i"): "-i",
    ("-1", "-i"): "i",
    ("-1", "j"): "-j",
    ("-1", "-j"): "j",
    ("-1", "k"): "-k",
    ("-1", "-k"): "k",

    ("i", "1"): "i",
    ("i", "-1"): "-i",
    ("i", "i"): "-1",
    ("i", "-i"): "1",
    ("i", "j"): "k",
    ("i", "-j"): "-k",
    ("i", "k"): "-j",
    ("i", "-k"): "j",


    ("-i", "1"): "-i",
    ("-i", "-1"): "i",
    ("-i", "i"): "1",
    ("-i", "-i"): "-1",
    ("-i", "j"): "-k",
    ("-i", "-j"): "k",
    ("-i", "k"): "j",
    ("-i", "-k"): "-j",

    ("j", "1"): "j",
    ("j", "-1"): "-j",
    ("j", "i"): "-k",
    ("j", "-i"): "k",
    ("j", "j"): "-1",
    ("j", "-j"): "1",
    ("j", "k"): "i",
    ("j", "-k"): "-i",


    ("-j", "1"): "-j",
    ("-j", "-1"): "j",
    ("-j", "i"): "k",
    ("-j", "-i"): "-k",
    ("-j", "j"): "1",
    ("-j", "-j"): "-1",
    ("-j", "k"): "-i",
    ("-j", "-k"): "i",

    ("k", "1"): "k",
    ("k", "-1"): "-k",
    ("k", "i"): "j",
    ("k", "-i"): "-j",
    ("k", "j"): "-i",
    ("k", "-j"): "i",
    ("k", "k"): "-1",
    ("k", "-k"): "1",

    ("-k", "1"): "-k",
    ("-k", "-1"): "k",
    ("-k", "i"): "-j",
    ("-k", "-i"): "j",
    ("-k", "j"): "i",
    ("-k", "-j"): "-i",
    ("-k", "k"): "1",
    ("-k", "-k"): "-1",

}

INVERSE = {
    "i": "-i",
    "j": "-j",
    "k": "-k"
}

if __name__ == "__main__":
    with open("C.in") as f:
        cnt = 0
        num_cases = int(f.readline())
        for i in xrange(num_cases):
            l, x = f.readline().split()
            l = int(l)
            x = int(x)
            initStr = f.readline().strip()
            dijkstraStr = "".join([initStr for j in xrange(x)])
#            print dijkstraStr
            ret = "NO"
            if len(dijkstraStr) >= 3:
                left = dijkstraStr[0]
                middle = dijkstraStr[1]
                right = dijkstraStr[2]
                for j in xrange(3, len(dijkstraStr)):
                    right = MULT[(right, dijkstraStr[j])]
                possibleMiddleRight = {(middle, right)}
                for j in xrange(2, len(dijkstraStr) - 1):
                    middle = MULT[(middle, dijkstraStr[j])]
                    right = MULT[INVERSE[dijkstraStr[j]], right]
                    possibleMiddleRight.add((middle, right))

                if left == "i" and ("j", "k") in possibleMiddleRight:
                    ret = "YES"
                else:
                    for j in xrange(1, len(dijkstraStr) - 2):
                        left = MULT[left, dijkstraStr[j]]
                        newPossibleMiddleRight = set()
                        for middle, right in possibleMiddleRight:
                            newPossibleMiddleRight.add(
                                (MULT[INVERSE[dijkstraStr[j]], middle], right)
                            )
                        possibleMiddleRight = newPossibleMiddleRight
                        if left == "i" and ("j", "k") in possibleMiddleRight:
                            ret = "YES"
                            break

            print "Case #%s: %s" % (i + 1, ret)