import sys

phrase = "welcome to code jam"
letters = set(phrase)

def nextline():
    return sys.stdin.readline().rstrip()

class Cell:
    def __init__(self, index):
        self._cost = 0
        self._index = index

    def get_index(self):
        return self._index

    index = property(get_index)

    def get_cost(self):
        return self._cost

    def set_cost(self, value):
        self._cost = value

    cost = property(get_cost, set_cost)

    def __str__(self):
        return "%s/%s" % (self.index, self.cost)

    def __unicode__(self):
        return unicode(self.index)

def solveRec(struc):
    if len(struc) == 1:
        return sum(map(lambda x: x.cost, struc[0]))

    line_prev = struc[0]
    line_next = struc[1]

    prev_cost = 0
    cursor = 0

    for cell in line_next:
        cell.cost = prev_cost

        for subcell in line_prev[cursor:]:

            if subcell.index < cell.index:
                break

            cell.cost = cell.cost + subcell.cost
            cursor = cursor + 1

        prev_cost = cell.cost

    struc = struc[1:]

    return solveRec(struc)

def solve(struc):
    for cell in struc[0]:
        cell.cost = 1

    return solveRec(struc)

def prepare_struc(str):
    str = filter(lambda c: c in letters, str)

    letter_dict = {}
    for l in letters:
        letter_dict[l] = list()

    index = 0
    for c in str:
        letter_dict[c].append(index)
        index = index + 1

    struc = list()
    for c in phrase:
        ls = list()
        ids = letter_dict[c]

        for i in ids:
            ls.append(Cell(i))

        struc.append(ls)

    struc.reverse()
    for line in struc:
        line.reverse()

    return struc

def print_struc(struc):
    print map(lambda l: map(lambda x: str(x), l), struc)

def doMain():
    count = int(nextline())
    for i in xrange(0, count):
        str = nextline()
        res = solve(prepare_struc(str))
        print "Case #%s: %04d" % (i + 1, res % 10000)

if __name__ == "__main__":
    doMain()

