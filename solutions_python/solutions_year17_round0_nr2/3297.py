def tidy(n, start):
    for i in range(start+1, len(n)):
        n[i] = 9

with open("B-large.in") as file, open("output", "w") as fp:
    case = 1
    cases = int(file.readline())
    while(case < cases + 1):
        integer = list(file.readline().rstrip('\n'))
        integer = list(map(int, integer))
        j = len(list(integer)) - 1
        while(j > 0):
            if(integer[j - 1] > integer[j]):
                integer[j - 1] -= 1
                tidy(integer, j - 1)
            j -= 1

        fp.write("Case #{}: ".format(case))
        fp.write(str(int(''.join(list(map(str, integer))))))
        fp.write("\n")

        case += 1