import sys


def get_input(filename):
    with open(filename, 'r') as f:
        T = int(f.readline())
        cases = []
        for t in range(T):
            S, K = f.readline().split()
            cases.append([list(S), int(K)])
        return T, cases


def print_output(res, T, filename):
    with open(filename, 'w') as f:
        for t in range(T):
            if res[t] == -1:
                line = "Case #{0}: IMPOSSIBLE".format(t+1)
            else:
                line = "Case #{0}: {1}".format(t+1, res[t])
            print(line)
            f.write(line + "\n")


def count_flip(s):
    [S, K] = s
    L = len(S)
    flips = 0
    for i in range(L-K+1):
        if S[i] == '-':
            flips += 1
            for j in range(K):
                S[i+j] = '-' if S[i+j] == '+' else '+'
    for i in range(K-1):
        if S[L-i-1] == '-':
            return -1
    return flips


if __name__ == '__main__':
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    T, cases = get_input(input_filename)
    res = [count_flip(s) for s in cases]
    print_output(res, T, output_filename)
