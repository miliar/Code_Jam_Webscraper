import os

def nofdigits(number):
    d = 0
    while number:
        d += 1
        number /= 10
    return d

def select(number, n, nth):
    return (number / 10**(n-nth))%10


def check(number):
    n = nofdigits(number)
    last = select(number, n, 1)
    for j in range(2, n+1):
        c = select(number, n, j)
        if c >= last:
            last = c
        else:
            return False
    return True

numbers = []
r = 0
number = 0
while number<1000:
    number += 1
    if check(number):
        #print("{}-{}".format(r+1, number))
        numbers.append(number)
        r += 1

with open(os.sys.argv[1], 'rb') as f:
    n_of_cases = int(f.readline().strip())
    for i in range(1, n_of_cases+1):
        n = int(f.readline().strip())
        idx = 0
        ln = 0
        while idx < len(numbers) and numbers[idx] <= n:
            ln = numbers[idx]
            idx += 1
        print("Case #{:d}: {:d}".format(i, numbers[idx-1]))




