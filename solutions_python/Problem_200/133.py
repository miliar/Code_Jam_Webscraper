inf = open('input.txt', mode='r')
outf = open('output.txt', mode='w')
cases = int(inf.readline())

for case in range(1, cases + 1):
    rstr = "Case #" + str(case) + ": "

    n = int(inf.readline())
    n_copy = n
    num = []
    while n_copy > 0:
        num.append(n_copy % 10)
        n_copy = n_copy // 10
    num.reverse()
    last = len(num)
    for i in range(len(num) - 2, -1, -1):
        if num[i] > num[i + 1]:
            num[i] -= 1
            last = i + 1
    for i in range(last, len(num)):
        num[i] = 9

    # print(num)
    res = int("".join([str(d) for d in num]))
    # print(res)
    rstr += str(res)
    print(rstr)
    outf.write(rstr + '\n')
