import sys

base_rate = 2.0

def cookie(c, f, x, b, t, cm):
    while(1):
        if x / b <= c / b:
            return x / b

        c1 = t + x / b
        c2 = t + c / b + x / (b + f)

        if c1 < c2:
            return c1

        t = t + c / b
        b = b + f
        cm = c2

def find_match(dataset):
    cases = []

    for i in range(1, dataset[0] + 1):
        data = dataset[i]
        cases.append(str(cookie(data['c'], data['f'], data['x'], base_rate, 0, data['x'] / base_rate)))

    return cases

def read_input(fname):
    f = open(fname, 'r')

    ncases = int(f.readline())

    dataset = []

    dataset.append(ncases)

    for i in range(ncases):
        data = {}

        ns = f.readline().split()

        data['c'] = float(ns[0])
        data['f'] = float(ns[1])
        data['x'] = float(ns[2])

        dataset.append(data)

    return dataset

def write_output(cases):
    for i in range(len(cases)):
        print "Case #" + str(i+1) + ":", cases[i]


def main():
    if len(sys.argv) != 2:
        print "Please specify an input file."
        return

    dataset = read_input(sys.argv[1])

    cases = find_match(dataset)

    write_output(cases)
    
if __name__ == "__main__":
    main()
