def readint(stream):
    return int(stream.next()[:-1])


def readline(stream):
    line = stream.next()[:-1]
    data = line.split(' ')
    return [(c == '+') for c in data[0]], int(data[1])


def main():
    with open('input.txt', 'r') as f:
        count = readint(f)
        with open('output.txt', 'w') as o:
            for i in range(count):
                arr, k = readline(f)
                o.write("Case #{}: {}\n".format(i + 1, solve(arr, k)))


def solve(arr, k):
    c = 0
    for i in range(len(arr) - k + 1):
        if arr[i]:
            continue
        c += 1
        for j in range(i, i + k):
            arr[j] = not arr[j]

    return c if all(arr) else 'IMPOSSIBLE'


if __name__=='__main__':
    main()