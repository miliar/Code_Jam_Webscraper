class Case:
    def __init__(self, stream):
        self.parse(stream)

    def parse(self, stream):
        index1 = int(stream.__next__().strip())
        rows1 = []
        for i in range(4):
            row = map(int, stream.__next__().strip().split(' '))
            row = set(row)
            rows1.append(row)
        index2 = int(stream.__next__().strip())
        rows2 = []
        for i in range(4):
            row = map(int, stream.__next__().strip().split(' '))
            row = set(row)
            rows2.append(row)

        self.index1 = index1
        self.rows1  = rows1
        self.index2 = index2
        self.rows2  = rows2

    def getAnswer(self):
        intersect = self.rows1[self.index1-1] & self.rows2[self.index2-1]
        if len(intersect) == 1:
            return list(intersect)[0]
        elif len(intersect) == 0:
            return "Volunteer cheated!"
        else:
            return "Bad magician!"


def main(filename):
    stream = open(filename, 'r')
    numCases = int(stream.__next__().strip())
    for n in range(numCases):
        case = Case(stream)
        msg = "Case #{0}: {1}".format(n+1, case.getAnswer())
        print(msg)

if __name__ == '__main__':
    main('A-small-attempt0.in')