import numpy


n = int(input())

target = open("./out.txt", 'w')

for case in range(n):
    s = input()
    rev = s
    #rev = s[::-1]
    rev = list(rev)

    for i in range(len(rev) - 1, 0, -1):
        if int(rev[i]) < int(rev[i - 1]):
            for j in range(i, len(rev)):
                rev[j] = '9'
            rev[i - 1] = str(int(rev[i - 1]) - 1)

    total = 0
    for index, x in enumerate(rev):
        total += (int(x) * pow(10, len(rev) - index - 1))

    target.write("Case #" + str(case + 1) + ": " + str(total) )
    target.write("\n")


target.close()
