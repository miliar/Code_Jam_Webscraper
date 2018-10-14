__author__ = 'MRajendran'
class MagicTrick:
    def setRow1(self, row):
        self.row1 = set([int(x) for x in row.split()])

    def setRow2(self, row):
        self.row2 = set([int(x) for x in row.split()])

    def result(self):
        chosen = self.row1 & self.row2
        if len(chosen) == 0:
            return 'Volunteer cheated!'
        elif len(chosen) == 1:
            return str(list(chosen)[0])
        else:
            return 'Bad magician!'

    def readInput(self, f):
        row = int(f.readline().strip())
        for i in range(row-1):
            f.readline()
        self.setRow1(f.readline().strip())
        for i in range(4-row):
            f.readline()
        row = int(f.readline().strip())
        for i in range(row-1):
            f.readline()
        self.setRow2(f.readline().strip())
        for i in range(4-row):
            f.readline()

m = MagicTrick()
fi = 'small'
f = open(fi +'.in')
o = open(fi + '.out','w')
cases = int(f.readline())
result = []

for i in range(cases):
    m.readInput(f)
    result.append(m.result())

index = 1
for r in result:
    o.write("Case #{0}: {1}\n".format(index,r))
    index += 1