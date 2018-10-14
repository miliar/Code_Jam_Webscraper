class Case(object):
    def __init__(self,lines):
        self.lines = lines
        self.alphabet = []

    def check_if_solvable(self):
        alphabet = [self.lines[0][0]]
        last = self.lines[0][0]
        for x in self.lines[0]:
            if x != last:
                alphabet.append(x)
                last = x
        for y in self.lines:
            last = y[0]
            if last != alphabet[0]:
                return False
            i=0
            for x in y:
                if x != last:
                    i+=1
                    try:
                        if x!= alphabet[i]:
                            return False
                    except:
                        return False
                    last = x
        if i+1 != len(alphabet):
            return False
        self.alphabet = alphabet
        return True

    def build_vector(self, line):
        count = 0
        ret = []
        last = line[0]
        for x in line:
            if x != last:
                ret.append(count)
                count = 0
                last = x
            count += 1
        ret.append(count)
        return ret

    def calculate_average(self, vec):
        sum = 0
        for x in vec:
            sum += x
        return sum / len(vec)

    def solve(self): 
        if not self.check_if_solvable():
            return 'Fegla Won'

        vectors = []
        for x in self.lines:
            vec = self.build_vector(x)
            vectors.append(vec)

        ret = 0
        for i in xrange(len(self.alphabet)):
            values = [x[i] for x in vectors]
            avg = self.calculate_average(values)
            for v in vectors:
                ret += abs(v[i]-avg)
        return ret





def parse_stdin():
    T = int(raw_input())
    cases = []
    for i in xrange(T):
        N = int(raw_input())
        lines = []
        for x in xrange(N):
            lines.append(raw_input())
        cases.append(Case(lines))
    return cases


def main():
    cases = parse_stdin()
    i = 1
    for c in cases:
        print 'Case #{:d}:'.format(i), c.solve()
        i += 1


if __name__ == '__main__':
    main()
