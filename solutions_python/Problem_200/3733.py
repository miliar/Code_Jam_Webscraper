from typing import List

def verify_tidy(digit_list: List[int]) -> bool:
    if find_tidy_error(digit_list) == -1:
        return True
    return False

def find_tidy_error(digit_list: List[int]) -> int:
    for i in range(0, len(digit_list) - 1):
        if digit_list[i] > digit_list[i+1]:
            return i
    return -1

def calculate_tidy(digit_list: List[int]):
    #We need to find the first instance where d(i) > d(i + 1)
    error_index = find_tidy_error(digit_list)

    if digit_list[error_index] == digit_list[error_index - 1]:
        #Walk backwards to find where d(i) > d(i - 1), if exists
        for i in range(error_index, -1, -1):
            error_index = i
            if error_index != 0 and digit_list[error_index] > digit_list[error_index - 1]:
                break

    #Just subtract the error index by 1
    digit_list[error_index] = digit_list[error_index] - 1
    
    #Set all remaining digits to 9
    for i in range(error_index + 1, len(digit_list)):
        digit_list[i] = 9
    
    return int("".join(map(str, digit_list)))


if __name__ == "__main__":
    cases = int(input())

    for case in range(0, cases):
        digit_list = [int(x) for x in input()]

        if not verify_tidy(digit_list):
            print("Case #{}: {}".format(case + 1, calculate_tidy(digit_list)))
        else:
            print("case #{}: {}".format(case + 1, int("".join(map(str, digit_list)))))
