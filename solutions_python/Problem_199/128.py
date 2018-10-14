inf = open('input.txt', mode='r')
outf = open('output.txt', mode='w')
cases = int(inf.readline())

for case in range(1, cases + 1):
    rstr = "Case #" + str(case) + ": "

    pan, k = inf.readline().split()
    k = int(k)
    pan = list(pan)
    n = len(pan)
    fail = False
    flips = 0
    for i in range(n):
        if pan[i] == '-':
            for j in range(i, i + k):
                if j >= n:
                    fail = True
                    break
                if pan[j] == '-':
                    pan[j] = '+'
                else:
                    pan[j] = '-'
            flips += 1
        if fail:
            break

    if fail:
        rstr += "IMPOSSIBLE"
    else:
        rstr += str(flips)
    print(rstr)
    outf.write(rstr + '\n')
