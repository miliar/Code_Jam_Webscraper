def flip_cake(string, i, k):
    for j in range(i, (i + k)):
        counter = 0

        if string[j] == '-':
            string[j] = '+'
        elif string[j] == '+':
            string[j] = '-'
            # print(j,i,k,string)
    return


def checkval(string):
    for i in range(0, len(string)):
        if string[i] == '-':
            return 0
    return 1


t = int(input())
for test in range(1, t + 1):
    array_num = input().strip().split()
    string = array_num[0]
    k = array_num[1]
    string = list(string)
    k = int(k)
    flag = 1
    count = 0
    for i in range(0, len(string)):
        if string[i] == '-' and (i + k) <= len(string):
            flip_cake(string, i, k)
            count = count + 1

        if checkval(string) is 1:
            print("Case #" + str(test) + ": " + str(count))
            flag = 0
            break
    if flag == 1:
        print("Case #" + str(test) + ": IMPOSSIBLE")

