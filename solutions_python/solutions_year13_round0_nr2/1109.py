import sys
import fileinput


def inc():
    i = 0
    while True:
        yield i
        i += 1


class Case:
    rows = None
    cols = None

    def __init__(self, dims):
        self.height = dims[0]
        self.width = dims[1]
        self.rows = []

    def addRow(self, row):
        self.rows.append([int(item) for item in row.split()])

    def genCols(self):
        cols = [[] for i in range(self.width)]

        for row in self.rows:
            for i in range(len(row)):
                cols[i].append(row[i])

        self.cols = cols
        print(cols)

    def row(self, index):
        return self.rows[index]

    def col(self, index):
        return self.cols[index]

    def arrayHasLarger(self, ary, val):
        return any(item > val for item in ary)

    def test(self):
        # Test each item in each row
        for y in range(self.height):
            row = self.row(y)
            for x in range(self.width):
                item = row[x]

                if self.arrayHasLarger(row, item):
                    col = self.col(x)
                    if self.arrayHasLarger(col, item):
                        return "NO"
                    else:
                        continue
                else:
                    continue
        return "YES"


def testCases(filename):
    result = ''
    i = inc()

    with fileinput.input(files=filename) as f:
        # Don't need the first line (number of cases)
        f.readline()

        line = f.readline()
        while line:
            case = Case([int(item) for item in line.split()])

            for y in range(case.height):
                case.addRow(f.readline())

            case.genCols()

            result += "Case #{}: {}\n".format(next(i) + 1, case.test())

            line = f.readline()

    return result


if __name__ == "__main__":
    filename = sys.argv[1]
    results = testCases(filename)

    output_file = open(filename.replace('in', 'out'), 'w')
    output_file.write(results)
    output_file.close()
