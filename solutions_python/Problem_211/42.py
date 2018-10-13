cases = int(raw_input())


class Rational(object):
    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return Rational.gcd(b, a % b)

    def __init__(self, num, den):
        g = Rational.gcd(num, den)
        self.num = num / g
        self.den = den / g

    def __add__(self, other):
        return Rational(self.num * other.den + self.den * other.num, self.den * other.den)

    def __sub__(self, other):
        return Rational(self.num * other.den - self.den * other.num, self.den * other.den)

    def __mul__(self, other):
        return Rational(self.num * other.num, self.den * other.den)

    def __div__(self, other):
        return Rational(self.num * other.den, self.den * other.num)

    def __lt__(self, other):
        return self.num * other.den < self.den * other.num

    def __hash__(self):
        return self.num * 18253 + self.den

    @staticmethod
    def parse(s):
        whole, deci = s.split(".")
        return Rational(int(whole) * 10000 + int(deci), 10000)


def evaluate(probs):
    product = Rational(1, 1)
    for key, value in probs.items():
        for x in xrange(value):
            product = product * key
    return product


def solve(probs, bonus):
    # print probs, bonus
    curr = {}
    for prob in probs:
        if prob in curr:
            curr[prob] += 1
        else:
            curr[prob] = 1

    while bonus > 0:
        smallest = Rational(100000, 1)
        second = Rational(100000, 1)
        for prob, mult in curr.items():
            if prob < smallest:
                second = smallest
                smallest = prob
            elif prob < second:
                second = prob
        needed = (second - smallest) * Rational(curr[smallest], 1)
        if bonus < needed:
            diff = bonus / Rational(curr[smallest], 1)
            newval = smallest + diff
            curr[newval] = curr[smallest]
            del curr[smallest]
            bonus = 0
        else:
            curr[second] += curr[smallest]
            del curr[smallest]
            bonus -= needed

    return evaluate(curr)

for ctr in xrange(cases):
    ss = raw_input().split(" ")
    n = int(ss[0])
    k = int(ss[1])
    bonus = Rational.parse(raw_input())
    ss = raw_input().split(" ")
    probs = []
    for s in ss:
        probs.append(Rational.parse(s))

    answer = solve(probs, bonus)
    flanswer = float(answer.num) / answer.den
    print "Case #{}: {:.10f}".format(ctr + 1, flanswer)
