import sys


def get_input(filename):
    with open(filename, 'r') as f:
        T = int(f.readline())
        cases = []
        for t in range(T):
            D, N = [int(x) for x in f.readline().split()]
            horses = []
            for n in range(N):
                horses.append([int(x) for x in f.readline().split()])
            cases.append([D, N, horses])
        return T, cases


def print_output(res, T, filename):
    with open(filename, 'w') as f:
        for t in range(T):
            line = "Case #{0}: {1}".format(t+1, round(res[t], 6))
            line = "Case #{0}: {1}".format(t+1, "{0:.6f}".format(res[t]))
            print(line)
            f.write(line + "\n")


def find_speed(s):
    [D, N, horses] = s
    t_max = 0
    for horse in horses:
        d = D-horse[0]
        s = horse[1]
        t = d/s
        if t > t_max:
            t_max = t
    return D/t_max


if __name__ == '__main__':
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    T, cases = get_input(input_filename)
    res = [find_speed(s) for s in cases]
    print_output(res, T, output_filename)
