
t = int(input())

for test_case in range(1, t+1):
    n = int(input())

    for integer in range(n, 0, -1):

        integer_str = str(integer)

        tidy = True
        for i in range(1, len(integer_str)):
            if integer_str[i] < integer_str[i-1]:
                tidy=False

        if tidy:
            last_tidy_num = integer
            print("Case #{}: {}".format(test_case, integer))
            break


