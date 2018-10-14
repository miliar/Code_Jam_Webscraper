
def getMax(a, b):
    res = 0;
    for i in xrange(a, b + 1):
        if isFairAndSquare(i):
            res += 1
    return res

def isFairAndSquare(number):
    root = number ** 0.5
    if (int(root) != root):
        return False

    st = str(int(root))
    for k in xrange(0, len(st)/2 + 1):
        if st[k] != st[-(k + 1)]:
            return False
    st = str(int(number))
    for k in xrange(0, len(st)/2 + 1):
        if st[k] != st[-(k + 1)]:
            return False
    return True


def main(filename):
    q = open(filename, "r")
    q.readline() #omit the first line
    result = open("fairandsquare_answer.txt", "w")
    t = 1
    for line in q:
        a, b = map(int, line.strip().split(" "))
        ans = getMax(a, b)
        print "Case #{0}: {1}".format(t, ans)
        result.write("Case #{0}: {1}\n".format(t, ans))
        t += 1
    result.close()
    q.close()

import cProfile
cProfile.run("main('fairandsquare.txt')")