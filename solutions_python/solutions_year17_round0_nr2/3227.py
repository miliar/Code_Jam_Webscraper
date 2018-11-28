# check the last digit with second last

t = int(input())
for test in range(1, t+1):
    num = int(input())

    digits = [int(d) for d in str(num)]

    if len(digits) is 1:
        print("Case #" + str(test) + ": " + str(int("".join(str(d) for d in digits))))
        continue

    for index in range(len(digits) - 1, 0, -1):
        if digits[index] < digits[index - 1]:

            if digits[index - 1] is 0:
                power = 1

                while digits[index - power] is 0:
                    # to reduce 1000 to 999

                    digits[index - power] = 9
                    power += 1

            digits[index - 1] = digits[index - 1] - 1

            for x in range(index, len(digits)):
                digits[x] = 9

    print("Case #"+ str(test) +": "+str(int( "".join(str(d) for d in digits) )))




