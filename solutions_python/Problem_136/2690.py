# Qualifications Part B
# Matt Maybeno 2014


def main(afile):
    numoftests, tests = readin(afile)
    allcases = []
    for num in xrange(numoftests):
        c, f, x = tests[num]
        produce = 2
        seconds = calc_sec(x, produce)
        secondsnew = calc_sec(x, produce)
        upgrade = 0
        while seconds >= secondsnew:
            seconds = upgrade + calc_sec(x, produce)
            upgrade += calc_sec(c, produce)
            produce += f
            secondsnew = upgrade + calc_sec(x, produce)

        allcases.append(seconds)
    outputcases(allcases)


def outputcases(allcases):
    """
    Outputs results as same as codejam
    """
    with open('b_out.txt', 'w') as f:
        for ncase, c in enumerate(allcases):
            f.write("Case #%s: %.7f\n" % (ncase+1, c))


def calc_sec(limit, produce):
    """Calculates seconds to complete"""
    return limit/produce


def str2int(l):
    """
    Converts row of ints in file to array
    """
    cleanstr = l.strip()
    splitstr = cleanstr.split()
    intlist = [int(u) for u in splitstr]
    return intlist


def str2float(l):
    """
    Converts row of floats in file to array
    """
    cleanstr = l.strip()
    splitstr = cleanstr.split()
    intlist = [float(u) for u in splitstr]
    return intlist


def readin(afile):
    """
    Read input file
    """
    tests = {}
    with open(afile) as f:
        testcase = str2int(f.next())[0]
        for x in range(testcase):
            answer = str2float(f.next())
            tests[x] = answer

    return [testcase, tests]


if __name__ == "__main__":
    main('B-large.in')