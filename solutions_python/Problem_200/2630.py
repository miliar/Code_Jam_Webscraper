def solve(num):
    if len(num) != 1:
        for i in range(len(num) - 1):
            if(num[i + 1] < num[i]):
                lastfound = i
                for j in range(1, i + 1):
                    if num[i - j] == num[i]:
                        lastfound = i - j
                num[lastfound] = num[lastfound] - 1
                for j in range(lastfound + 1, len(num)):
                    num[j] = 9

    if num[0] == 0:
        num = num[1:]
    return ''.join(map(str, num))


with open('input.txt', 'r') as f:
    with open('output.txt', 'w') as fw:
        c = int(f.readline())
        for i in range(c):
            num = list(map(int, list(f.readline()[:-1])))
            res = solve(num)
            fw.write("Case #{}: {}\n".format(i + 1, res))
