def flip(row, k):
    pancakes = []
    for c in row:
        pancakes.append(True if c == '+' else False)
    i = 0
    flips = 0
    for i in range(len(pancakes)-k+1):
        if not pancakes[i]:
            flips += 1
            for j in range(i, i+k):
                pancakes[j] = not pancakes[j]
    if all(pancakes):
        return flips
    else:
        return 'IMPOSSIBLE'


if __name__ == '__main__':
        with open('output.out', 'w') as out:
            input()
            case = 0
            while True:
                case += 1
                try:
                    pancakes = input()
                except:
                    break
                row, k = pancakes.split(' ')
                ans = flip(row, int(k))
                out.write('Case #{:}: {:}\n'.format(case, ans))
