import string

def tidy_numbers(case_number, n, f):
    tidy_number = n

    sorted_number = list(tidy_number)
    sorted_number.sort()

    while list(tidy_number) != sorted_number:
        tidy_number = str(int(tidy_number) - 1)
        sorted_number = list(tidy_number)
        sorted_number.sort()

    answer = 'Case #{}: {}'.format(case_number, tidy_number)

    print(answer)
    f.write(answer + '\n')  # python will convert \n to os.linesep


if __name__ == '__main__':
    lines = [line.strip('\n') for line in open('./B-small-attempt0.in')]
    f = open('B-small-attempt0.out', 'w')

    i = 1
    for line in lines[1:]:
        tidy_numbers(i, line, f)
        i += 1

    f.close()  # you can omit in most cases as the destructor will call it