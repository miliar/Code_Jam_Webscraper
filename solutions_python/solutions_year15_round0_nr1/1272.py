__author__ = 'Mohan.Rajendran'
def solve(prob):
    Smax = int(prob.split()[0])
    S = prob.split()[1]
    friends = 0
    count = 0

    for required,s in enumerate(S):
        if required > count:
            friends += (required - count)
            count += (required - count)
        count += int(s)

    return friends

if __name__ == "__main__":
    fileName = "large"
    inp = open(fileName + '.in', 'r')
    outp = open(fileName + '.out', 'w')

    cases = int(inp.readline())

    for case in xrange(1, cases+1):
        prob = inp.readline()
        outp.write("Case #%i: %s\n" % (case, solve(prob)))

    inp.close()
    outp.close()