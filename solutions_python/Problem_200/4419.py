def check(num):
    if len(str(num)) == 1:
        return num

    none = 0
    while True:
        for i in range(0, (len(str(num))) - 1):

            if str(num)[i] > str(num)[i+1]:
                num = num - 1
                break

            elif str(num)[i] <= str(num)[i+1] and i+1 == len(str(num)) - 1 and none != 1:
                return num


row_count = 0
number = int(input())
for i in range(number):
    num = int(input())
    func_out = check(num)
    print("Case #{}: {}".format(i+1, func_out))