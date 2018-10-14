##########################
#  Google Code Jam 2017  #
#     Tidy Numbers       #
# Written by Jake Herman #
##########################

def find_tidy_num(number: str) -> int:
    previous_digit = int(number[0])
    cur_digit = 0
    all_same = True

    for num in number:
        if int(num) < previous_digit and not all_same:
            return (str(int(number[:cur_digit]) - 1) + ('9' * len(number[cur_digit:]))).lstrip('0')
        elif int(num) < previous_digit and all_same:
            return (str(previous_digit - 1) + ('9' * (len(number) - 1))).lstrip('0')

        if int(num) != previous_digit:
            all_same = False

        previous_digit = int(num)
        cur_digit += 1

    return number

def generate_file(file: open) -> None:
    file.readline()
    case_num = 1

    for case in file.readlines():
        print("Case #{}: {}".format(case_num, find_tidy_num(case.strip("\n"))))
        case_num += 1

if __name__ == '__main__':
    generate_file(open('B-small-attempt0.in'))
    #print(find_tidy_num('7'))

"""
def is_tidy_num(number: str) -> bool:
    previous_num = int(number[0])
    for num in number:
        if int(num) < previous_num:
            return False
        previous_num = int(num)
    return True

def find_tidy_num(number: str) -> int:
    for i in range(int(number), 0, -1):
        if is_tidy_num(str(i)):
            return i
"""