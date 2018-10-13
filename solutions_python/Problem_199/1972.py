def solved(row):
    for i in range(len(row)):
        if row[i] == '-':
            return False
    return True


def flip(row, idx, length):
    s = ''
    for i in range(len(row)):
        if idx <= i <= idx + length - 1:
            s += '+' if row[i] == '-' else '-'
        else:
            s += row[i]
    return s


class Cases:
    def __init__(self, path):
        f = open(path, 'r')

        num_cases = int(f.readline())
        self.cases = []

        for i in range(num_cases):
            line = f.readline().split(' ')
            self.cases.append(Case(line[0], int(line[1])))

        f.close()

    def __str__(self):
        s = ''
        for i in range(len(self.cases)):
            s += str(self.cases[i])
        return s

    def solve(self, path):
        f = open(path, 'w')
        solutions = ''
        for i in range(len(self.cases)):
            solutions += 'Case #' + str(i+1) + ': ' + self.cases[i].solve() + '\n'
        f.write(solutions[:-1])
        f.close()


class Case:
    def __init__(self, row, length):
        self.row = row
        self.length = length

    def __str__(self):
        return self.row + ' ' + str(self.length)

    def solve(self):
        count = 0
        idx = 0
        while not solved(self.row):
            if idx + self.length > len(self.row):
                return 'IMPOSSIBLE'
            if self.row[idx] == '-':
                self.row = flip(self.row, idx, self.length)
                count += 1
            idx += 1
        return str(count)
