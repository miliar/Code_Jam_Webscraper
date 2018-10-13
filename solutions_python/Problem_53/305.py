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

ON_OFF = {True:'ON', False:'OFF'}

class SnapperCase(TestInput):
    def __init__(self, input_stream):
        super(SnapperCase, self).__init__(input_stream)
        N, K = self.read(int, int)
        self.result = ON_OFF[self.is_on(N, K)]

    def is_on(self, N, k):
        bstate = bin(k)
        state = [bstate[i] for i in range(2, len(bstate))]
        state.reverse()
        if len(state)<N:
            state += [0]*(N-len(state))
        state = state[0:N]
        p = 0
        while p < len(state) and state[p] == '1':
            p += 1
        return p == N

class SnapperTester(TestInput):
    def __init__(self, input_stream):
        super(SnapperTester, self).__init__(input_stream)
        N = self.read(int)
        for c in range(N):
            case = SnapperCase(input_stream)
            print "Case #%d: %s" % (c+1, case.result)

st=SnapperTester(sys.stdin)
