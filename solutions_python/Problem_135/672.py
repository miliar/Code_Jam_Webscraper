import sys, getopt

def getResult(r1, r2, case):
    res = []
    ans_string = 'Case #{case}: {ans}'
    for elm in r1:
        if elm in r2:
            res.append(elm)

    if len(res) == 1:
        return ans_string.format(case=case, ans=res[0])
    elif len(res) > 1:
        return ans_string.format(case=case, ans='Bad magician!')
    else:
        return ans_string.format(case=case, ans='Volunteer cheated!')

def main(argv):
    out = open('out.txt', 'w')
    f = open(argv[0], 'r')
    testcases = int(f.readline())

    for case in xrange(testcases):
        ans1 = int(f.readline())
        row1, row2 = [], []
        for i in range(4):
            currentRow = f.readline()
            if i == (ans1 - 1):
                row1 = [int(x) for x in currentRow.split()]

        ans2 = int(f.readline())

        for i in range(4):
            currentRow = f.readline()
            if i == (ans2 - 1):
                row2 = [int(x) for x in currentRow.split()]

        res = getResult(row1, row2, case + 1)
        print res
        out.write(res + '\n')

    out.close()
    f.close()

if __name__ == "__main__":
   main(sys.argv[1:])