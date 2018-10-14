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


class Case:
    def __init__(self, row):
        values = row.split(' ')
        self.num_stalls = int(values[0])
        self.num_people = int(values[1])

    def __str__(self):
        return str(self.num_stalls) + ' ' + str(self.num_people)

    def solve(self):
        stalls = [0,self.num_stalls+1]
        last_dist = 0
        for i in range(self.num_people):
            idx = 0
            dist = 0
            for j in range(len(stalls)-1):
                if stalls[j+1] - stalls[j] > dist:
                    dist = stalls[j+1] - stalls[j]
                    last_dist = dist
                    idx = j
            stalls = stalls[:idx+1] + [stalls[idx]+(dist//2)] + stalls[idx+1:]
        return str((last_dist - 1)//2) + ' ' + str((last_dist - 2)//2)
