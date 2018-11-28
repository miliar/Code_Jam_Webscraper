import sys


def solve(lst, K):
    new_interval = None
    for i in range(K):
        _max_idx = lst.index(max(lst))
        _max = lst[_max_idx]

        if _max % 2 != 0:
            new_interval = [(_max - 1) // 2] * 2
        else:
            new_interval = [_max // 2 - 1, _max // 2]

        lst[_max_idx:_max_idx+1] = new_interval
    new_interval.sort(reverse=True)
    return ' '.join(list(map(str, new_interval)))


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        src = f.read()

    lines = src.splitlines()
    T = int(lines.pop(0))

    result = ''
    for i in range(T):
        N, K = lines.pop(0).split(maxsplit=1)
        result += 'Case #{idx}: {result}\n'.format(idx=i+1, result=solve([int(N)], int(K)))

    #print(result)
    with open('output.txt', 'w') as f:
        f.write(result)
