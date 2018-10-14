def flip(x):
    return '+' if x == '-' else '-'


for x in range(int(input())):
    _pancakes, _k = input().split()
    pancakes = list(_pancakes)
    k = int(_k)
    f = 0
    n = len(pancakes)
    for i in range(n):
        if pancakes[i] == '-':
            if i > n - k:
                result = 'IMPOSSIBLE'
                break
            pancakes[i] = '+'
            pancakes[i + 1:i + k] = [flip(j) for j in pancakes[i + 1:i + k]]
            f += 1
    else:
        result = f
    print('Case #{}: {}'.format(x + 1, result))
