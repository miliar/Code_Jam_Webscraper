t = int(input())

for i in range(1, t + 1):
    n = [int(s) for s in input()]
    total = len(n)
    index = total - 1

    while(index > 0):
        if n[index] < n[index - 1]:
            j = index
            n[j - 1] -= 1
            while(j < total):
                n[j] = 9
                j += 1
        index -= 1

    print('Case #{}: {}'.format(i, ''.join(str(digit) for digit in n).lstrip('0')))