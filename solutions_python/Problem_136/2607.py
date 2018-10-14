import fileinput


eps = 10e-6

def process(line):
    tmp = line.split()
    C, F, X = float(tmp[0]), float(tmp[1]), float(tmp[2])

    (own, t, V) = (0, 0, 2.0)

    ts = [10000000.0]
    while 1:
        if own-X > eps:
            return t

        t1 = t + (X-own)/V
        t2 = t + C/V + (X-own)/(V+F)

        if t1 > t2:
            own = 0
            t += C/V
            V += F
        else:
            ts.append(t1)
            own = 0
            t = t + C/V + C/(V+F)
            V += (2*F)
        min_t = min(ts)
        ts = [min_t]

        if t > min_t:
            return min_t


def main():
    fin = fileinput.input()
    T = int(next(fin)) # number of test cases
    for case in range(1, T+1):
        line = next(fin).strip()
        cost = process(line)
        print("Case #{}: {}".format(case, cost))


if __name__ == '__main__':
    main()
