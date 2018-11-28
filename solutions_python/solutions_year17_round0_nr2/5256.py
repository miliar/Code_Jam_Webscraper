import sys


f = open(sys.argv[1], 'r')
numbers = f.read().splitlines()
case_number = 1
for n in numbers:
    tidy_number_found = False
    while tidy_number_found is False:
        digit_list = []
        for digit in str(n):
            digit_list.append(int(digit))
            print(digit_list)
        if len(digit_list) == 1:
            tidy_number_found = True
            break
        is_accending = False
        for i in range(len(digit_list) - 1):
            if digit_list[i] <= digit_list[i+1]:
                is_accending = True
            else:
                is_accending = False
                break
        tidy_number_found = is_accending
        n = int(n) - 1

    if (int(n) > 10):
        n = int(n) + 1
    string_n = str(n)
    print("Case #{}: {}".format(str(case_number), string_n))
    output = open(sys.argv[2], 'a')
    output.writelines("Case #{}: {}\n".format(str(case_number), string_n))
    case_number += 1
