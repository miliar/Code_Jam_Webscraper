

class Case(object):

    def __init__(self, Number, S, K):
        self.Number = Number
        self.S = S
        self.K = K
        self.M = 0

    def __repr__(self):
        return "Case #{}: {}".format(self.Number, self.M)

    def solve(self):
        length = len(self.S)
        for i, c in enumerate(self.S):
            if c == '-':
                if (length - i) < self.K:
                    self.M = 'IMPOSSIBLE'
                    break
                self.flip_at(i)
                self.M += 1
     
    def flip_at(self, index):
        for i in range(self.K):
            c = self.S[index + i]
            self.S[index + i] = '+' if c == '-' else '-'


def read_inputs():
    T = int(raw_input())
    inputs = []
    for case in xrange(1, T + 1):
        S, K = raw_input().split(" ")
        inputs.append(Case(case, list(S), int(K)))
    return inputs



inputs = read_inputs()
for i in inputs:
    i.solve()
    print i



