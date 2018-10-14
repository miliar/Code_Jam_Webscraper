def extend(options, x, V):
    newOptions = set()
    for y in options:
        if x+y <= V:
            newOptions.add(x+y)
    return options | newOptions

def countNewCoins(uncovered, options, V):
    lst = list(uncovered)
    lst.sort()
    i = 0
    for x in lst:
        if x in options:
            continue
        i += 1
        options = extend(options, x, V)
        if len(options) == V+1:
            return i
    return i


class Case:
    @classmethod
    def parse(cls, stream):
        line1 = next(stream).strip()
        line2 = next(stream).strip()

        C, D, V = map(int, line1.split())
        coins = list(map(int, line2.split()))

        return cls(C, V, coins)

    def __init__(self, C, V, coins):
        self.C = C
        self.V = V
        self.coins = set(coins)

    def solve(self):
        options = {0}
        V = self.V
        for x in self.coins:
            options = extend(options, x, V)

        if self.C == 1:
            uncovered = set(range(V+1)) - options
            return countNewCoins(uncovered, options, V)
        else:
            raise NotImplementedError()
            newCoins = 0

        return newCoins

def main(finname, foutname=None):
    fin = open(finname, 'r')
    fout = None if foutname==None else open(foutname, 'w')
    count = int(next(fin).strip())
    for i in range(count):
        case = Case.parse(fin)
        answer = case.solve()
        print("Case #{}: {}".format(i+1, answer), file=fout)

if __name__ == '__main__':
    main("C-small-attempt2.in", "C-small-attempt2.out")
    #main("input.txt")
