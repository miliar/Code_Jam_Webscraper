import sys

class Reader:
    def __init__(self, filename):
        self.fp = open(filename)

    def read(self):
        tokens = self.fp.readline().split()
        result = []
        for token in tokens:
            try:
                result.append(int(token, 10))
            except ValueError:
                result.append(token)
        return result

if __name__ == '__main__':
    reader = Reader(sys.argv[1])
    case_count, = reader.read()
    for case in xrange(case_count):
        wire_count, = reader.read()
        wires = []
        for i in xrange(wire_count):
            start, end = reader.read()
            wires.append((start, end))
        wires.sort()
        ends = [end for (start, end) in wires]
        # bubble sort and keep track of swap count
        swap_count = 0
        while True:
            swapped = False
            for j in xrange(len(ends) - 1):
                if ends[j] > ends[j + 1]:
                    ends[j], ends[j + 1] = ends[j + 1], ends[j]
                    swap_count += 1
                    swapped = True
            if not swapped:
                break
        assert ends == sorted(ends)

        print "Case #%d: %d" % (case + 1, swap_count)
