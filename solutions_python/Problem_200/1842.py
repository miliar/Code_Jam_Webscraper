import sys


def get_input(filename):
    with open(filename, 'r') as f:
        T = int(f.readline())
        cases = []
        for t in range(T):
            S = f.readline().rstrip()
            cases.append([int(x) for x in S])
        return T, cases


def print_output(res, T, filename):
    with open(filename, 'w') as f:
        for t in range(T):
            line = "Case #{0}: {1}".format(t+1, res[t])
            print(line)
            f.write(line + "\n")


def find_biggest_tidy(N):
    L = len(N)
    i = 0
    while i < L-1 and N[i] <= N[i+1]:
        i += 1
    if i == L-1:
        return int(''.join(str(x) for x in N))
    while i >= 0 and N[i] > N[i+1]:
        N[i] = N[i]-1
        i -= 1
    i += 2
    while i < L:
        N[i] = 9
        i += 1
    return int(''.join(str(x) for x in N))


if __name__ == '__main__':
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    T, cases = get_input(input_filename)
    res = [find_biggest_tidy(N) for N in cases]
    print_output(res, T, output_filename)
