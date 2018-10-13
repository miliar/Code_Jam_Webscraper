import fileinput
from collections import defaultdict

def read_problem():
    f = fileinput.input()
    N = int(f.readline())
    for i in range(1, N+1):
        C = defaultdict(dict)
        O = {}
        L = f.readline().split()
        nc = int(L[0])
        for c in L[1:nc+1]:
            assert len(c) == 3
            C[c[0]][c[1]] = c[2]
            C[c[1]][c[0]] = c[2]
        del L[:nc+1]
        no = int(L[0])
        for o in L[1:no+1]:
            assert len(o) == 2
            O[o[0]] = o[1]
            O[o[1]] = o[0]
        del L[:no+1]
        assert len(L) == 2
        yield i, (C, O, L[-1])

def solve(Combine, Oppose, Invoke):
    result = []
    for inv in Invoke:
        # try combine.
        if result:
            try:
                result[-1] = Combine[inv][result[-1]]
                continue
            except KeyError:
                pass
        # Then, try oppose
        pair = Oppose.get(inv)
        if pair is not None and pair in result:
            del result[:]
        else:
            result.append(inv)
    return result

def format_result(result):
    return '[' + ', '.join(result) + ']'

def main():
    for case, problem in read_problem():
        print "Case #%d:" % case, format_result(solve(*problem))

if __name__ == '__main__':
    main()
