def printResult(result, number):
    print('Case #{}: {}'.format(number, result))

for tc in range(int(input().strip())):
    n = list(input().strip())
    if len(n) == 1:
        printResult(int(''.join(n)), tc + 1)
        continue
    isTidy = False
    while not isTidy:
        for i in range(len(n) - 1, -1, -1):
            if int(n[i - 1]) > int(n[i]) and not i == 0:
                n[i:] = ['9'] * (len(n) - i)
                n[i - 1] = str(int(n[i - 1]) - 1)
                break
            if i == 0:
                isTidy = True
    printResult(int(''.join(n)), tc + 1)


