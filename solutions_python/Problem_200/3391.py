
class Case(object):

    def __init__(self, Number, N):
        self.Number = Number
        self.N_list = [int(i) for i in str(N)]

    def __repr__(self):
        tidy = "".join([str(d) for d in self.N_list])
        return "Case #{}: {}".format(self.Number, tidy)

    def solve(self):
        index = self.find_non_tidy_position()
        while index >= 0:
            self.make_tidy_at(index)
            index = self.find_non_tidy_position()

    def find_non_tidy_position(self):
        for i in range(len(self.N_list) - 1):
            if self.N_list[i] > self.N_list[i+1]:
                return i
        return -1

    def make_tidy_at(self, index):
        self.N_list[index] -= 1
        for i in range(index + 1, len(self.N_list)):
            self.N_list[i] = 9
        if self.N_list[0] == 0:
            del(self.N_list[0])


def read_inputs():
    T = int(raw_input())
    inputs = []
    for case in xrange(1, T + 1):
        N = raw_input()
        inputs.append(Case(case, int(N)))
    return inputs



inputs = read_inputs()
for i in inputs:
    i.solve()
    print i



