from itertools import combinations

def find_min_dens(C, V, dens):
    check = [False for i in range(V)]
    for i in range(0, len(dens)):
        for j in map(sum, combinations(dens, i + 1)):
            if j - 1 < len(check):
                check[j - 1] = True

    additions = 0
    while True:
        try:
            n = check.index(False)
            check[n] = True

            additions += 1

            for i, e in enumerate(check[:]):
                if e:
                    try:
                        if i == n:
                            for k in range(1, C):
                                check[i + (n + 1) * k] = True
                        else:
                            for k in range(1, C + 1):
                                check[i + (n + 1) * k] = True
                    except IndexError:
                        continue
        except ValueError:
            return additions

def test_solution():
    assert find_min_dens(1, 6, [1, 2, 5]) == 0

def solve(f_in, line):
    xs = list(map(int, line.split()))
    C, D, V = xs[0], xs[1], xs[2]

    dens = f_in.readline()

    dens = list(map(int, dens.split()))

    return "{}".format(find_min_dens(C, V, dens))


















































if __name__ == '__main__': 
    import fileinput

    with fileinput.input() as f_input:
        f_input.readline()
        for i, line in enumerate(f_input, 1):
            result = solve(f_input, line)
            print("Case #{}: {}".format(i, result))

