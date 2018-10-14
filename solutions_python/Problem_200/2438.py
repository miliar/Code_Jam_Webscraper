TEST_FILE = 'B-large.in'

def main():

    f = open(TEST_FILE, 'r')
    s = open('tn-output-large.txt', 'w')
    num_test_cases = int(f.readline())

    for test_case in range(1, num_test_cases+1):
        number = int(f.readline())

        result = solve(number)
        s.write('Case #{}: {}\n'.format(test_case, result))

    f.close()
    s.close()



def solve(num):
    print('num:', num, '-----------------------')

    n_list = [int(i) for i in str(num)]

    while not check_non_decreasing(n_list):

        for index, digit in enumerate(n_list[:-1]):
            current_digit = n_list[index]
            next_digit = n_list[index + 1]

            if current_digit > next_digit:
                n_list[index] -= 1
                for i in range(index+1, len(n_list)):
                    n_list[i] = 9

    result = int(''.join(map(str, n_list)))

    return result

def check_non_decreasing(n_list):


    if len(n_list) == 1:
        return True

    for index, digit in enumerate(n_list[:-1]):
        if n_list[index] > n_list[index+1]:
            return False

    return True



if __name__ == '__main__':
    main()