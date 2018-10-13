
def input_list(file_name):
    results = []
    with open(file_name, 'r') as reader:
        T = int(next(reader).strip())
        for ind in range(T):
            line = next(reader)
            strs = line.strip().split(' ')
            (D, N) = (int(strs[0]), int(strs[1]))

            horses = []
            for num in range(N):
                line = next(reader)
                strs = line.strip().split(' ')
                horses.append((int(strs[0]), int(strs[1])))

            results.append(solve(D, N, horses))
    reader.close()
    return results


def solve(D, N, horses):
    if N == 1:
        (K1, S1) = horses[0]
        S = float(D * S1)/(D - K1)

    elif N == 2:
        (K1, S1) = horses[0]
        (K2, S2) = horses[1]
        if not(S2 == S1):
            KM = float(K1 * S2 - K2 * S1)/(S2 - S1)
        else:
            KM = 0
        if KM >= max(K1, K2):
            if KM >= D:
                if K1 < K2:
                    S = (D * S1)/(D - K1)
                else:
                    S = (D * S2)/(D - K2)
            else:
                S = D / ((KM-K1)/S1 + (D-KM)/min(S1, S2))
        else:
            if K1 < K2:
                S = float(D * S1) / (D - K1)
            else:
                S = float(D * S2) / (D - K2)
    return "{:10.6f}".format(S)


def print_line(ind, r):
    return 'Case #{}: {}\n'.format(ind, r)


if __name__ == '__main__':
    results = input_list('A-small-attempt0.in')

    f = open('A-small-0.out', 'w')
    ind = 1
    for r in results:
        f.write(print_line(ind, r))  # python will convert \n to os.linesep
        ind += 1
    f.close()
