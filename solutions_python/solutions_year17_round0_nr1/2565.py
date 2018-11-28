from fileinput import input

data = input('A-large.in')

for case in range(int(next(data))):
    pancakes, k = next(data).split()
    pancakes = list(pancakes)
    k = int(k)
    result = 0
    for i in range(len(pancakes) - k + 1):
        if pancakes[i] == '-':
            result += 1
            for j in range(i, i + k):
                if pancakes[j] == '-':
                    pancakes[j] = '+'
                else:
                    pancakes[j] = '-'

    for i in range(len(pancakes) - k, len(pancakes)):
        if pancakes[i] == '-':
            result = 'IMPOSSIBLE'
            break

    print('Case #{}: {}'.format(case + 1, result))
