#
# IMPORTS
#
import fileinput

data = fileinput.input()
n = int(data[0])

# check number input
def check (n, i):
    if i == 0:
        return n

    if (n[i] >= n[i - 1]):
        n = check(n, i - 1)

    else:
        n[i] = '9'
        n[i - 1] = str(int(n[i - 1]) - 1)
        for j in range(i + 1, len(n)):
            n[j] = '9'
        n = check(n, i - 1)

    return n
# check()

# iterate through inputs
for i in range(1, n + 1):
    number = data[i]
    algarisms = list(number)
    del algarisms[len(algarisms) - 1]
    result = check(algarisms, len(algarisms) - 1)
    result = ''.join(result)
    print('Case #{0}: {1}'.format(i, int(result)))
