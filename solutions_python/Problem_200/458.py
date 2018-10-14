def naive(N):
    i = int(N)
    while sorted(str(i)) != list(str(i)):
        i -= 1
    return str(i)

def smart(N):
    digits = list(map(int, N))
    for i in range(len(digits) - 2, -1, -1):
        if digits[i] > digits[i + 1]:
            digits[i] -= 1
            digits[i + 1:] = [9] * len(digits[i + 1:])
    return ''.join(map(str, digits)).lstrip('0')

T = int(input())
for x in range(1, T + 1):
    N = input()
    print('Case #{}: {}'.format(x, smart(N)))
