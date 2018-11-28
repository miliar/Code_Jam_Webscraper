import sys

class TestInput(object):
    def __init__(self, input_stream):
        self.input_stream = input_stream
    def readline(self):
        return self.input_stream.readline().strip()
    def read(self, *args):
        words = self.readline().split()
        result = []
        for i in range(len(args)):
            result.append(args[i](words[i]))
        if len(args) == 1:
            return result[0]
        return result
    def read_list(self, atype):
        words = self.readline().split()
        return map(atype, words)


class RollerCoasterCase(TestInput):
    def __init__(self, input_stream):
        super(RollerCoasterCase, self).__init__(input_stream)
        self.R, self.k, self.N = self.read(int, int, int)
        self.g = self.read_list(int)
        self.qs = 0;
        self.euros = 0
        for r in range(self.R):
            self.load_coaster()
        self.result = "%d"%self.euros

    def load_coaster(self):
        i = self.qs
        people = 0
        while True:
            people += self.g[i]
            if people > self.k:
                people -= self.g[i]
                break
            i += 1
            if i == self.N:
                i = 0
            if i == self.qs:
                break
        self.euros += people
        self.qs = i


class RollerCoasterTester(TestInput):
    def __init__(self, input_stream):
        super(RollerCoasterTester, self).__init__(input_stream)
        T = self.read(int)
        for c in range(T):
            case = RollerCoasterCase(input_stream)
            print "Case #%d: %s" % (c + 1, case.result)

rtc=RollerCoasterTester(sys.stdin)
