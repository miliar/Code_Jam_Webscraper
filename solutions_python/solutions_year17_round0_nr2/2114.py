def decrease(number, idx):
    s = ''
    finished = False
    i = idx
    while not finished and i >= 0:
        n = int(number[i]) - 1
        if n >= 0:
            finished = True
        else:
            n = 9
            i -= 1
        s = str(n) + s
    for j in range(i-1, -1, -1):
        s = number[j] + s

    for i in range(idx+1, len(number)):
        s += '9'

    finished = False
    while not finished:
        if s[0] == '0':
            s = s[1:]
        else:
            finished = True
    return s


def is_tidy(number):
    for i in range(len(number)-1):
        if number[i] > number[i+1]:
            return False
    return True


class Cases:
    def __init__(self, path):
        f = open(path, 'r')

        num_cases = int(f.readline())
        self.cases = []

        for i in range(num_cases):
            self.cases.append(Case(f.readline()))
        f.close()

    def __str__(self):
        s = ''
        for i in range(len(self.cases)):
            s += str(self.cases[i]) + '\n'
        return s[:-1]

    def solve(self, path):
        f = open(path, 'w')
        solutions = ''
        for i in range(len(self.cases)):
            solutions += 'Case #' + str(i+1) + ': ' + self.cases[i].solve() + '\n'
        f.write(solutions[:-1])
        f.close()

    def test(self, path):
        f = open(path, 'w')
        solutions = ''
        for i in range(len(self.cases)):
            solutions += 'Case #' + str(i+1) + ': ' + self.cases[i].test() + '\n'
        f.write(solutions[:-1])
        f.close()


class Case:
    def __init__(self, row):
        if row[-1] == '\n':
            self.number = row[:-1]
        else:
            self.number = row

    def __str__(self):
        return str(self.number)

    def solve(self):
        i = 0
        while i < len(self.number)-1:
            if int(self.number[i]) > int(self.number[i+1]):
                self.number = decrease(self.number, i)
                i = 0
            else:
                i += 1
        return self.number

    def test(self):
        n = self.number
        while not is_tidy(n):
            n = str(int(n)-1)
        return str(n)
