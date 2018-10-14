from math import sqrt

i = open('C-small-attempt0.in', 'r')
o = open('fair-square-result.txt', 'w')

def cases():
    n_cases = int(i.next())
    for x in range(n_cases):
        line = i.next()
        s, f = line.split()
        yield (int(s), int(f))


def run():
    for i, (start, finish) in enumerate(cases()):
        print(start,finish)
        num_matches = 0
        for x in range(start, finish + 1):
            if str(x) == "".join(reversed(str(x))):
                y = str(sqrt(x))
                if y.endswith(".0"):
                    y = y[:-2]
                if y == "".join(reversed(y)):
                    print(x)
                    num_matches += 1

        print("matches: {num_matches}".format(**locals()))
        a = i + 1
        o.write("Case #{a}: {num_matches}\n".format(**locals()))


run()

