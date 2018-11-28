class Case:
    def __init__(self, line):
        numbers = map(float, line.split(' '))
        (self.c, self.f, self.x) = numbers

    def solve(self):
        C = self.c
        F = self.f
        X = self.x
        time = 0.0
        speed = 2.0

        timeWithFarm = C/speed + X/(speed + F)
        timeNoFarm = X/speed
        while timeWithFarm < timeNoFarm:
            time += C/speed
            speed += F
            timeWithFarm = C/speed + X/(speed + F)
            timeNoFarm = X/speed

        return time + X/speed


def main(filename, output=None):
    stream = open(filename, 'r')
    numCases = int(next(stream).strip())
    for n in range(1, numCases+1):
        case = Case(next(stream))
        print("Case #{0}: {1:.7f}".format(n, case.solve()), file=output)

if __name__ == '__main__':
    output = open('b-large.output.txt', 'w')
    main('B-large.in', output)
    print("Done!")
