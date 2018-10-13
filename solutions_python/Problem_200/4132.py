# Problem 02 - Tidy Numbers


read = open('B-small-attempt3.in', 'r')
write = open('B-small-attempt3.out', 'w')


# noinspection PyPep8Naming
def check(N2):
    listN = list(N2)
    for i in range(0, len(listN)):
        for j in range(i, len(listN)):
            if not int(listN[i]) <= int(listN[j]):
                return False
    return True


N = 0
T = 0
line_count = -1
Case = 0
finished = False

for line in read:
    line_count += 1
    if int(line_count) is 0:
        T = line
    elif int(line_count) <= int(T):
        N = int(line)
        N_Temp = N
        Case += 1
        while not finished:
            if check(str(N_Temp)):
                write.write('Case #' + str(Case) + ': ' + str(N_Temp) + '\n')
                finished = True
            else:
                N_Temp -= 1
        finished = False

read.close()
write.close()
