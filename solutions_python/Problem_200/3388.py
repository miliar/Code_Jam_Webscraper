n = int(input())

for i in range(1, n + 1):
    cur = 0
    output = list(input())
    if output[-1] == '\n':
        output = output[:-1]
    for x in range(len(output) - 1):
        num1 = int(output[x])
        num2 = int(output[x+1])
        if num1 > num2:
            for y in range(x, -1, -1):
                if int(output[y]) > int(output[y + 1]) or int(output[y + 1]) == 0:
                    output[y + 1] = '9'
                    output[y] = str(int(output[y]) - 1)[0]
                else:
                    break
            for y in range(x+1, len(output)):
                output[y] = '9'
            break

    answer = ''.join(output)
    if answer[0] == '0':
        answer = answer[1:]

    print("Case #{}: {}".format(i, answer))