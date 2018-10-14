import sys

class Wizard(object):
    def __init__(self, combined, oposed):
        self.combined = combined
        self.oposed = oposed
        self.data = []

    def __str__(self):
        out = ['[']
        out = ', '.join(self.data)
        return '[' + out + ']'
    
    def invoke(self, elem):
        if not self.data:
            self.data.append(elem)
            return
        if self.try_to_combine(elem):
            return
        if self.verify_oposed(elem):
            return

        self.data.append(elem)

    def try_to_combine(self, elem):
        combined = self.combined.get(self.data[-1]+elem)
        if combined:
            self.data[-1] = combined
            return True
        return False

    def verify_oposed(self, elem):
        oposed = self.oposed.get(elem)
        if oposed in self.data:
            self.data = []
            return True
        return False


def solve_line(case, line):
    combined = {}
    oposed = {}

    c = int(line.pop(0))
    while c:
        elements = line.pop(0)
        combined[elements[0]+elements[1]] = elements[2]
        combined[elements[1]+elements[0]] = elements[2]
        c -= 1
    
    d = int(line.pop(0))
    while d:
        elements = line.pop(0)
        oposed[elements[0]] = elements[1]
        oposed[elements[1]] = elements[0]
        d -= 1

    wizard = Wizard(combined, oposed)

    n = int(line.pop(0))
    string = line.pop(0)
    for elem in string:
        wizard.invoke(elem)
    
    print "Case #%s: %s" % (case, wizard)


if __name__ == '__main__':
    filename = sys.argv[1]

    with open(filename) as fileobj:
        t = int(fileobj.readline())
        for i in xrange(t):
            line = fileobj.readline().strip().split()
            solve_line(i+1, line)
