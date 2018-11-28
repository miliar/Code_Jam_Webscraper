from sys import argv


def response(n, candidates):
    l = len(candidates)
    s = None

    if l == 1: s = candidates[0];
    elif l > 1: s = "Bad magician!";
    else: s = "Volunteer cheated!";
    
    return "Case #{}: {}".format(n+1, s)


def run_test(lines):
    a1 = int(lines[0])
    a2 = int(lines[5])
    r1 = set(lines[a1].split(' '))
    r2 = set(lines[a2+5].split(' '))

    return list(r1.intersection(r2))


if __name__ == '__main__':
    INPUT = open(argv[1] if len(argv) > 1 else "/tmp/shiner")
    lines = [x.strip() for x in INPUT.readlines()]

    num_tests = lines.pop(0)

    for i in xrange(0, len(lines), 10):
        print response(i/10, run_test(lines[i:i+10]))

        

