# Program:   Tidy numbers
# Author:    Somdeep Datta


T = int(input())
cases = []

for i in range(T):                                  # iterate test cases
    cases.append(int(input()))

for i in cases:
    largest = 0
    for j in range(i, 0, -1):                       # iterate through N
        flag = 0
        number = j
        while number != 0:
            dig1 = number % 10
            dig2 = int(number/10) % 10
            if dig1 >= dig2:
                number = int(number/10)
                flag = 1
                continue
            flag = 0
            break

        if flag:
            largest = j
            break

    print("Case #{0}: {1}".format(cases.index(i)+1, largest))