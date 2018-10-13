import math

c = int(input())
T = c

def isTidy(num):
    num_str = str(num)

    for i in range(len(num_str) - 1):
        if num_str[i] > num_str[i+1]:
            return (False, i)

    return (True, -1)

def isTidyAndNoZero(num):
    res = isTidy(num)
    # print(num)
    # print(res[0])
    # print(bool(num % 10))
    bool_val = bool(num % 10) and res[0]

    return ( bool_val , res[1] )

while T:
    T -= 1
    num = int(input())
    while (not isTidyAndNoZero(num)[0]):
        prob = isTidyAndNoZero(num)[1]
        str_num = str(num)
        temp_num = str_num[:prob]
        dec_digit = str(int(str_num[prob]) - 1)
        left_digits = "9" * (len(str_num) - prob - 1)
        temp_num += dec_digit + left_digits

        num =int(temp_num)

    ans = int(num)

    print("Case #" + str(c-T) + ": " + str(ans))

# for i in range(4654):
#     print(str(i) + " " + str(isTidyAndNoZero(i)))

