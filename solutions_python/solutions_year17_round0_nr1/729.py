def flip(start, k, s):
    for i in range(start, start+k):
        s[i] = (s[i] + 1) % 2


def solve(s, k):
    result = 0
    for i, c in enumerate(s):
        if i == len(s) - k + 1:
            break
        if c == 0:
            flip(i, k, s)
            result += 1
        # print(i, s)
    if 0 in s:
        result = 'IMPOSSIBLE'
    return result


def save(i, result):
    print(f'Case #{i}: {result}')


def main():
    t = int(input())
    for i in range(t):
        s, k = input().split()
        s = [1 if c == '+' else 0 for c in s]
        result = solve(s, int(k))
        save(i+1, result)


if __name__ == '__main__':
    main()
