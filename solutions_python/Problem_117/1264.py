
def analyze(testcase):
    nbrows, nbcols = len(testcase), len(testcase[0])
    maxrows = [max(row) for row in testcase]
    maxcols = [max(col) for col in zip(*testcase)]
    for i in range(nbrows):
        for j in range(nbcols):
            if testcase[i][j] < maxrows[i] and testcase[i][j] < maxcols[j]:
                return "NO"
    return "YES"

def parse_input(filename):
    testcases = []
    with open(filename, "rb") as f:
        lines = f.readlines()
    nb = int(lines[0])
    current_line = 1
    for n in range(nb):
        nrows, ncols = [int(s) for s in lines[current_line].split(" ")]
        testcase = []
        for i in range(nrows):
            testcase.append([int(s) for s in lines[current_line + 1 + i].split(" ")])
        testcases.append(testcase)
        current_line += nrows + 1
    return testcases

def print_result(testcases):
    res = ""
    for i, test in enumerate(testcases):
        res += "Case #%d: %s\n" % (i+1, analyze(test))
    return res

testcases = parse_input("B-large.in")
output = print_result(testcases)
print output

with open("result_large.txt", "wb") as fout:
    fout.write(output)
