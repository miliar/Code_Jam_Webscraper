def main():
    number_of_tests = int(input())
    for case_number in range(1, number_of_tests + 1):
        case_data = int(input())
        case_result = solve(case_data)
        print(f'Case #{case_number}: {case_result}')


def solve(case_data):
    case_data_numbers = [int(each_number) for each_number in str(case_data)]
    while True:
        for position, (digit, next_digit) in enumerate(zip(case_data_numbers, case_data_numbers[1:])):
            if digit > next_digit:
                break
        else:
            # Tidy Number Found
            return int(''.join(str(each_number) for each_number in case_data_numbers))

        # subtract 1 from current position to attempt getting tidy number
        case_data_numbers[position] -= 1
        for trailing_position in range(position+1, len(case_data_numbers)):
            case_data_numbers[trailing_position] = 9


if __name__ == '__main__':
    main()
