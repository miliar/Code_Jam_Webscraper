
def main():
    file = open('B-large.in', 'rU')
    lines = iter(file.readlines())
    file.close()

    case_count = int(next(lines))

    for case_idx in range(0, case_count):

        digits = list(next(lines).rstrip())

        stop = len(digits) - 1
        did_change = True

        while did_change:
            did_change = False

            for idx in range(stop):
                if did_change:
                    digits[idx] = '9'
                elif digits[idx] > digits[idx + 1]:
                    did_change = True
                    digits[idx] = str(int(digits[idx]) - 1)
                    digits[stop] = '9'
                    stop = idx

        if digits[0] == '0':
            digits = digits[1:]

        digits_str = ''.join(digits)
        print(f'Case #{case_idx  + 1}: {digits_str}')


if __name__ == '__main__':
    main()
