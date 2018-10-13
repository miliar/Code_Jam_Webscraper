

def solve(shyness):
    standing = 0
    added = 0

    for t in xrange(0, len(shyness)):
        if shyness[t] == 0:
            continue

        if standing >= t:
            standing += shyness[t]
        else:
            added += t - standing
            standing = t + shyness[t]

    return added


def main():
    f1 = open('ovation.out', 'w')

    with open('ovation.in', 'r') as f:
        cases = int(f.readline())

        for t in xrange(1, cases + 1):
            case = f.readline()

            case = case.strip('\n')

            _, digits = case.split(' ')

            shyness = map(int, list(digits))

            print >>f1, "Case #" + str(t) + ": " + str(solve(shyness))

if __name__ == '__main__':
    main()