import itertools
from operator import mul

class InputScanner(object):

    def __init__(self, filename, parse_function):
        with open(filename) as f:
            self.reversed_lines = list(reversed(f.read().split('\n')))
        self.case_count = 0
        self.total_cases = self.next_int()
        self.parse_function = parse_function

    def __iter__(self):
        for i in range(self.total_cases):
            yield self.next_case()

    def next_int(self):
        return int(self.reversed_lines.pop())
    
    def next_line(self):
        return self.reversed_lines.pop()

    def next_matrix(self):
        (h, w) = map(int, self.next_line().split())
        return tuple(tuple(self.next_line()) for i in range(h))

    def next_case(self):
        p = self.parse_function(self)
        self.case_count += 1
        return p

class Solver(object):

    def __init__(self, solver_function, input_scanner, out=None):
        self.solver_function = solver_function
        self.out = out
        self.input_scanner = input_scanner

    def solve(self):
        for case in iter(self.input_scanner):
            print >> self.out, 'Case #%s: %s' % (self.input_scanner.case_count,
                                                 self.solver_function(case))

def main(input_filename, out=None):
    input_scanner = InputScanner(input_filename, parse_function)
    Solver(solver_function, input_scanner, out).solve()


########################################################################

def parse_function(scanner):
    (typed, lenght) = map(int, scanner.next_line().split())
    probs = map(float, scanner.next_line().split())
    return (typed, lenght, probs)

def solver_function(case):
    (typed, lenght, probs) = case

    medias = []
    for i in range(0, typed + 1):
        medias.append(solve(typed, lenght, probs, i))
        medias.append(enter(typed, lenght, probs, i))    
        
    return str('%.6f' % min( medias))

def enter(typed, lenght, probs, bks):
    result = lenght + 2
    if typed == lenght:
        p = reduce(mul, probs, 1)
        return result * (1 - p) + (lenght + 1) * p
    #print result
    return result

def solve(typed, lenght, probs, bks):
    if bks == 0:
        correct = reduce(mul, probs, 1)
        strokes = lenght - typed + 1
        #print strokes, correct,
        incorrect_strokes = strokes + lenght + 1
        result = correct * strokes + (1 - correct) * incorrect_strokes
        #print result
        return result

    else:
        result = solve(typed - 1, lenght, probs[:-1], bks - 1) + 1
        return result

if __name__ == '__main__':
    #main('sample.in')
    with open('out.txt', 'w') as out: main('A-small-attempt0 (1).in', out)
    print 'Done'


