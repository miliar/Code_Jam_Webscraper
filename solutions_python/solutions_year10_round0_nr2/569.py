import sys

def GCD(a, b):
    if (b == 0):
        return a
    return GCD(b, a % b)

L = 0
for line in sys.stdin:
    if L == 0:
        pass
    else:
        numbers = [int(item) for item in line.split()]
        T = numbers[2]-numbers[1]
        for n in numbers[3:]:
            T = GCD(T, n - numbers[1])
        if T < 0:
            T = -T
        if numbers[1]%T==0:
            y = 0
        else:
            y = T - numbers[1]%T
        sys.stdout.write('Case #' + str(L) + ': ' + str(y) + '\n')
    L += 1
