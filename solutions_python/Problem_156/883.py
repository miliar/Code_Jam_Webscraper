

class PancakeSolver(object):
    def __init__(self):
        self.memo = {}

    def pancake(num ):

        if num in self.memo:
            return self.memo[num]
        
        normal = 0
        special = 0

        for i in range((num / 2) + 1):
            pass

        return normal, special

class MySolver(object):
    def __init__(self):
        self.memo = {}
        """
        self.memo[1] = (1, 0)
        self.memo[2] = (2, 0)
        self.memo[3] = (3, 0)
        self.memo[4] = (2, 1)
        self.memo[5] = (2, 2)
        self.memo[6] = (3, 1)
        self.memo[7] = (3, 2)
        self.memo[8] = (2, 3)
        self.memo[9] = (3, 2)
        """

        self.memo[1] = None
        self.memo[2] = None
        self.memo[3] = None
        self.memo[4] = ([3, 1], [2, 2])
        self.memo[5] = ([4, 1], [3, 2])
        self.memo[6] = ([5, 1], [4, 2], [3, 3])
        self.memo[7] = ([6, 1], [5, 2], [4, 3])
        self.memo[8] = ([7, 1], [6, 2], [5, 3], [4, 4])
        self.memo[9] = ([8, 1], [7, 2], [6, 3], [5, 4])
        

    def pancake(self, diners, calls):
        normal = max(diners)

        if calls > 10:
            return normal + calls

        l = self.memo[normal]
        if l:
            best = 100
            for combi in l:
                temp = list(diners)
                temp.remove(normal)
                temp.extend(combi)

                special = self.pancake(temp, calls + 1)

                if special < best:
                    best = special

            if best < normal + calls:
                return best
            
            """
            temp = list(diners)
            temp.remove(normal)
            temp.extend(l)
        
            special = self.pancake(temp, calls + 1)

            if special < normal + calls:
                return special
            """
            
        return normal + calls

def parse(input_lines):
    n_cases = int(input_lines.pop(0))
    cases = []

    for i in range(0, len(input_lines), 2):
        if input_lines[i]:
            c = input_lines[i + 1].split(' ')
            c = [int(item) for item in c]
            cases.append(c)

    return n_cases, cases

def solve(input_file):
    with open(input_file + '.in', 'r') as f:
        input_lines = f.read().split('\n')

    n_cases, cases = parse(input_lines)

    solver = MySolver()

    solution = []
    for i in range(0, n_cases):
        #answer = solve_case(cases[i])
        answer = solver.pancake(cases[i], 0)
        solution.append('Case #%s: %s' % (i + 1, answer))

    with open(input_file + '.out', 'w') as f:
        f.write('\n'.join(solution))

if __name__ == '__main__':
    solve('B-small-attempt2')
    print 'Done!'
    #pass
