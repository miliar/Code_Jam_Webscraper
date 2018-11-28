import copy
names = ['R', 'O', 'Y', 'G', 'B', 'V']

def solve(colors):
    total = colors[0]
    total1 = colors[0]
    colors = colors[1:]
    last = -1
    result = []
    while total:
        current_max = 0
        current = None
        for idx, num in enumerate(colors):
            if idx != last and num > current_max:
                current_max = num
                current = idx
            elif len(result) and idx != last and num == current_max and idx == result[0]:
                current = idx
        if current is None:
            return 'IMPOSSIBLE'
        result.append(current)
        colors[current] -= 1
        last = current
        total -= 1
    if total1 > 1 and result[0] == result[-1]:
        return 'IMPOSSIBLE'
    return ''.join(map(lambda x: names[x], result))

def main():
    T = input()
    for i in xrange(1, T + 1):
        colors = map(int, raw_input().strip().split())
        print 'Case #{0}: {1}'.format(i, solve(colors))

if __name__ == '__main__':
    main()
