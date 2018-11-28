import sys

def nextline():
    return sys.stdin.readline().rstrip()

class MapEntry:

    def __init__(self, i, j):
        self._altitude = 0
        self._mark = 0
        self._row = i
        self._column = j

    def get_altitude(self):
        return self._altitude

    def set_altitude(self, value):
        self._altitude = value

    altitude = property(get_altitude, set_altitude)

    def get_mark(self):
        return self._mark

    def set_mark(self, value):
        self._mark = value

    mark = property(get_mark, set_mark)

    def get_row(self):
        return self._row

    row = property(get_row)

    def get_column(self):
        return self._column

    column = property(get_column)


class Map:

    def __init__(self, h, w):
        self.altitudes = []
        self._h = h
        self._w = w

        for i in xrange(0, h):
            row = list()
            self.altitudes.append(row)

            for j in xrange(0, w):
                row.append(MapEntry(i, j))

    def get_w(self):
        return self._w

    def get_h(self):
        return self._h

    def __getitem__(self, key):
        (r,c) = key
        return self.altitudes[r][c]

    def get_sinks(self):
        for i in xrange(0, self._h):
            for j in xrange(0, self._w):
                cell = self.get_if_sink(i, j)

                if cell:
                    yield cell

    def get_if_sink(self, i, j):
        cell = self[(i, j)]
        neighbours = self.get_neighbours(cell)

        for n in neighbours:
            if n.altitude < cell.altitude:
                return None

        return cell

    def get_lowest(self, cell):
        neighbours = self.get_neighbours(cell)
        lowest = cell

        for neighbour in neighbours:
            if neighbour.altitude < lowest.altitude:
                lowest = neighbour

        if lowest == cell:
            return None

        return lowest

    def get_neighbours(self, cell):
        (i, j) = (cell.row, cell.column)

        if i > 0:
            yield self[(i - 1, j)]
        if j > 0:
            yield self[(i, j - 1)]
        if j < self._w - 1:
            yield self[(i, j + 1)]
        if i < self._h - 1:
            yield self[(i + 1, j)]

def readMap():
    (h,w) = map(int, nextline().split(' '))

    aMap = Map(h, w)

    for row in xrange(0, h):
        aRow = map(int, nextline().split(' '))

        for column in xrange(0, w):
            aMap[(row, column)].altitude = aRow[column]

    return aMap

def mark_bound_neighbours(aMap, cell):
    neighbours = aMap.get_neighbours(cell)

    for neighbour in neighbours:
        lowest = aMap.get_lowest(neighbour)

        if lowest == cell:
            neighbour.mark = cell.mark
            mark_bound_neighbours(aMap, neighbour)


def solve(aMap):
    def letter_gen():
        for c in "abcdefghijklmnopqrstuvwxyz":
            yield c

    next_mark = 1
    sinks = list(aMap.get_sinks())
    labels = {}
    next_letter = letter_gen()

    for sink in sinks:
        sink.mark = next_mark
        next_mark = next_mark + 1

    for sink in sinks:
        mark_bound_neighbours(aMap, sink)

    for i in xrange(0, aMap.get_h()):
        for j in xrange(0, aMap.get_w()):
            cell = aMap[(i, j)]

            if not cell.mark in labels:
                labels[cell.mark] = next_letter.next()

    for i in xrange(0, aMap.get_h()):
        for j in xrange(0, aMap.get_w()):
            sys.stdout.write("%s" % labels[aMap[(i, j)].mark])
            if j < aMap.get_w() - 1:
                sys.stdout.write(" ")
        sys.stdout.write("\n")


def doMain():
    count = int(nextline())

    for mapCounter in xrange(0, count):
        print "Case #%s:" % (mapCounter + 1)
        aMap = readMap()
        solve(aMap)

if __name__ == "__main__":
    doMain()
