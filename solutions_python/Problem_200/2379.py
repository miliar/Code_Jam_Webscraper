def run():
    loop = input()
    for i in range(int(loop)):
        str_number = input()
        answer = solve(str_number)
        write(answer, i)

def solve(str_number):
    tmp_num = '0'
    is_tidy = True
    tidy_index = 0
    for index, n in enumerate(str_number):
        num = n
        if num > tmp_num:
            tmp_num = num
            tidy_index = index
        elif num == tmp_num:
            continue
        else:
            is_tidy = False
            break
    return str_number if is_tidy else get_tidy(str_number, tidy_index)

def get_tidy(str_number, tidy_index):
    return strip_leading_zero(str_number[:tidy_index] +
            get_one_number_tidy(str_number[tidy_index]) +
            ('9' * (len(str_number) - tidy_index - 1)))

def get_one_number_tidy(n):
    n = int(n)
    if n == 0:
        return '9'
    else:
        return str(n - 1)

def strip_leading_zero(str_num):
    if str_num.startswith('0') and len(str_num) != 1:
        return str_num[1:]
    else:
        return str_num

def write(answer, i):
    print('Case #{i}: {answer}'.format(answer=answer, i=(i+1)))


if __name__ == '__main__':
    run()
