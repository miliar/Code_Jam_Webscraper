#!/usr/bin/env python3
def main():
    testcases = int(input())
    for i in range(testcases):
        upper_bound = int(input())
        tidy_result = find_tidy_number_below(upper_bound)
        print_case(i, tidy_result)

def print_case(case_zero_based, result):
    string = 'Case #' + str(case_zero_based + 1) + ': ' + str(result)
    print(string)

def find_tidy_number_below(n):
    candidate = int2list(n)

    is_tidy = False
    while not is_tidy:
        is_tidy, candidate = decrease_if_not_tidy(candidate)
    return representation2int(candidate)

def decrease_if_not_tidy(candidate):
    is_tidy = True
    for pos in range(len(candidate) - 1):
        if int(candidate[pos]) > int(candidate[pos + 1]):
            is_tidy = False
            candidate = create_new_candidate(pos, candidate)
            break
    return [is_tidy, candidate]

def create_new_candidate(pos, stringlist):
    digit = int(stringlist[pos])
    new_digit = digit - 1 if digit > 0 else 9

    new_stringlist = stringlist[:]
    new_stringlist[pos] = str(new_digit)
    for i in range(pos + 1, len(stringlist)):
        new_stringlist[i] = '9'
    new_stringlist = refresh_representation(new_stringlist)
    return new_stringlist

def int2list(n):
    return list(str(n))

def refresh_representation(stringlist):
    string = ''.join(stringlist)
    integer = int(string)
    return int2list(integer)

def representation2int(stringlist):
    return int(''.join(stringlist))

if __name__ == '__main__':
    main()
