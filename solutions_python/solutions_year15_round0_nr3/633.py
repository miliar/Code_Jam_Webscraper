from sys import stdin, stdout

identityTable = {
    "i": {"j": "k", "k": "j-"},
    "j": {"i": "k-", "k": "i"},
    "k": {"i": "j", "j": "i-"},
}

class Quat:
    def __init__(self):
        self.sign = 1
        self.char = ""

    def combineChar(self, other):
        if not self.char:
            self.char = other

        elif other == self.char:
            self.sign *= -1
            self.char = ""

        else:
            result = identityTable[self.char][other]
            self.char = result[0]
            
            if len(result) > 1:
                self.sign *= -1

    def equalsChar(self, other):
        return self.sign == 1 and self.char == other

    def equalsConst(self, other):
        return not self.char and self.sign == other

    def __repr__(self):
        return "%s, %s"%(self.sign, self.char)


def check(patt, X):
    dummyPatt = patt * X

    checkAccum = Quat()
    for ch in dummyPatt:
        checkAccum.combineChar(ch)

    return checkAccum.equalsConst(-1)


def simple(patt, X):
    dummyPatt = patt * X

    xAccum = Quat()
    for i in range(len(dummyPatt)):
        xAccum.combineChar(dummyPatt[i])

        if xAccum.equalsChar("i"):
            yAccum = Quat()
            for j in range(i+1, len(dummyPatt)):
                yAccum.combineChar(dummyPatt[j])

                if yAccum.equalsChar("j"):
                    zAccum = Quat()
                    for k in range(j+1, len(dummyPatt)):
                        zAccum.combineChar(dummyPatt[k])

                    if zAccum.equalsChar("k"): # must go to end
                        return True

    return False



T = int(stdin.readline())
iteration = 0

while (iteration != T):

    _, X = map(int, stdin.readline().strip().split())

    patt = "".join(stdin.readline().strip().split())

    if not check(patt, X):
        result = "NO"

    else:
        if simple(patt, X):
            result = "YES"
        else:
            result = "NO"

    iteration += 1
    print "Case #%d: %s"%(iteration, result)
