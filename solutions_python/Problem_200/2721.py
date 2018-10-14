def sol_print(value):
    sol_print.line_number += 1
    print "Case #%d: %s"%(sol_print.line_number, value)


def is_tidy(number):
    max_idx = len(number) - 1
    for idx, value in enumerate(number):
        if idx < max_idx:
            if int(number[idx]) > int(number[idx + 1]):
                return False
    return True


def get_last_tidy_number(number):
    tidy_number = ""
    max_idx = len(number) - 1
    for idx, value in enumerate(number):
        if idx < max_idx:
            # idx + 1 dispo
            a = int(number[idx])
            b = int(number[idx + 1])
            if a > b:
                #TODO take care about 0,
                tidy_number += str(a - 1)
                for _ in range(idx + 1, max_idx + 1):
                    tidy_number += str('9')
                if not is_tidy(tidy_number):
                    return get_last_tidy_number(tidy_number)
                return tidy_number
            else:
                tidy_number += str(a)
    else:
        #TODO if else not needed ?
        return number


def main():
    sol_print.line_number = 0
    lines = int(raw_input())
    for number in range(lines):
        input_number = str(raw_input())
        tidy_number = get_last_tidy_number(input_number)
        sol_print(int(tidy_number))


if __name__ == "__main__":
    main()
