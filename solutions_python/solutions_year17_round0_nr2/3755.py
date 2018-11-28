# Google Code Jam
# Qualification Round
# Problem B - Tidy numbers
# Ing. S. Van Dessel
# 2017-04-08

FILE_IN = "B-large.in"
FILE_OUT = "B-large.out"


def tidy(x):
    for i in range(1, len(x)):
        if x[i] < x[i-1]:
            return False
    return True


def problem(x):
    for i in range(1, len(x)):
        if x[i-1] > x[i]:
            if x[i-1] == 0:
                print('This can never be the case, but just to make sure...')
            return i
    print('No problem found.')
    return i


def do_case(nb):
    if tidy(nb):                                # check if digits are already tidy
        return nb
    while not tidy(nb):
        i = problem(nb)
        nb[i-1] -= 1
        nb[i:] = [9]*len(nb[i:])
    return nb


def main():
    solution = ''
    with open(FILE_IN, 'r') as f:
        f.readline()
        for i, line in enumerate(f):
            number = map(int, line.strip())         # get next number
            digits = list(number)                   # split number in list of digits
            tidy_digits = do_case(digits)           # calculate digits of last tidy number
            tidy_number = int(''.join(map(str, tidy_digits)))       # merge digits into number
            print(tidy_number)                                      # print number
            solution += "Case #{}: {}\n".format(i+1, tidy_number)   # add number to solution

    solution = solution[:-1]                        # remove last new line
    with open(FILE_OUT, 'w') as f:                  # write solution
        f.write(solution)


if __name__ == '__main__':
    main()
