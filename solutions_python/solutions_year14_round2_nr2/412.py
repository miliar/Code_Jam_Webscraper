import math

class Solver():
    def __init__(self, f):
        parts = f.readline().split(' ')
        self.a = int(parts[0])
        self.b = int(parts[1])
        self.k = int(parts[2])

    def zero_parts(self):
        true_k = self.k - 1
        floored = int(math.log(true_k, 2))
        num_perms = floored * (2 ** floored)
        ways_to_get_zero = 0
        return ways_to_get_zero * num_perms

    def brute_force(self):
        poss = 0
        for i in xrange(self.a):
            for j in xrange(self.b):
                if i & j < self.k:
                    poss += 1
        return poss

    def solve(self):
        return str(self.brute_force())


def main():
    with open('input.txt', 'rb') as f:
        num_problems = int(f.readline())
        answers = []
        for i in xrange(num_problems):
            solver = Solver(f)
            answers.append('Case #%d: %s' % (i + 1, solver.solve()))
            print "done with %d" % i
        with open('output.txt', 'w') as fout:
            fout.write('\n'.join(answers))
        print answers


if __name__ == "__main__":
    main()
