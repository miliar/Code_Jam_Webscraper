import sys


def get_input(filename):
    with open(filename, 'r') as f:
        T = int(f.readline())
        cases = []
        for t in range(T):
            N, K = [int(x) for x in f.readline().split()]
            cases.append([N, K])
        return T, cases


def print_output(res, T, filename):
    with open(filename, 'w') as f:
        for t in range(T):
            line = "Case #{0}: {1} {2}".format(t+1, res[t][0], res[t][1])
            print(line)
            f.write(line + "\n")


def split_space(N):
    if N == 1:
        return []
    elif N == 2:
        return [1]
    elif N % 2 == 1:
        return [N/2, N/2]
    else:
        return [N/2, N/2-1]


def get_last_space(N):
    if N == 1:
        return [0, 0]
    elif N == 2:
        return [1, 0]
    elif N % 2 == 1:
        return [N/2, N/2]
    else:
        return [N/2, N/2-1]


def get_stalls_repartition(S):
    [N, K] = S
    spaces = [N]
    for i in range(K-1):
        spaces = sorted(spaces[1:] + split_space(spaces[0]), reverse=True)
    return get_last_space(spaces[0])


if __name__ == '__main__':
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    T, cases = get_input(input_filename)
    res = [get_stalls_repartition(S) for S in cases]
    print_output(res, T, output_filename)
