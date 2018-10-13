def solve():
    inp, k = input().split()
    k = int(k)
    num = 0
    vals = [c == '+' for c in inp]
    while len(vals) >= k:
        if vals[-1]:
            vals.pop()
        else:
            num += 1
            for i in range(-k, 0):
                vals[i] = not vals[i]
    if all(vals):
        return num
    else:
        return 'IMPOSSIBLE'


def main():
    t = int(input())
    for i in range(t):
        print('Case #{}: {}'.format(i + 1, solve()))


if __name__ == '__main__':
    main()
