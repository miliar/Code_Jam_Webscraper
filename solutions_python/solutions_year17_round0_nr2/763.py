import sys


def ninify(start, n):
    n[start:] = [9] * (len(n) - start)


def solve(n: list):
    init = ''.join(map(str, n))
    last = 10

    for i in range(len(n)-1, -1, -1):
        if n[i] > last:
            n[i] -= 1
            ninify(i + 1, n)
        last = n[i]

    for i in range(len(n)):
        if n[i] == 0:
            n = n[1:]
        else:
            break
    result = ''.join(map(str, n))
    print(f'>  {init}\n   {result}\n', file=sys.stderr)
    return result


def save(i, result):
    print(f'Case #{i}: {result}')


def main():
    t = int(input())
    for i in range(t):
        result = solve([int(n) for n in input()])
        save(i+1, result)


if __name__ == '__main__':
    main()
