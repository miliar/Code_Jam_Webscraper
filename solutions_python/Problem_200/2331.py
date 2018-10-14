def get_tidy_number(number, start_idx=None):
    num_list = list(str(number))
    if start_idx is None:
        start_idx = len(num_list)

    prev_digit = 10
    if len(num_list) > 1:
        for idx in range(start_idx)[::-1]:
            curr_digit = int(num_list[idx])
            #print curr_digit, 'vs', prev_digit
            # so far it's tidy
            if  curr_digit <= prev_digit:
                # set prev_digit
                prev_digit = curr_digit
                # set this idx to '9' in case it isn't tidy after all
                num_list[idx] = '9'

            # not tidy
            else:
                num_list[idx] = str(abs(curr_digit - 1))
                number = ''.join(num_list)

                # recurse
                return get_tidy_number(int(number), idx+1)

    return number

def main():
    filename = 'B-large.in'

    with open(filename, 'r') as input_file:
        num_tests = int(input_file.readline().strip())
        test_number = 1

        while test_number <= num_tests:
            ans = get_tidy_number(int(input_file.readline()))
            print 'Case #{}: {}'.format(test_number, ans)

            test_number += 1

if __name__ == '__main__':
    main()
