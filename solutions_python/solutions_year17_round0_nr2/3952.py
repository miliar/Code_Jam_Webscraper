import sys


def is_tidy(number):
    return all(
        number[i] <= number[i+1] for i in range(len(number)-1)
    )


def main():
    num_cases = int(sys.stdin.readline().strip())
    for case_num in range(1, num_cases + 1):
        last_number = int(sys.stdin.readline().strip())

        while not is_tidy(str(last_number)):
            last_number = last_number - 1

        print('Case #{}: {}'.format(case_num, last_number))


if __name__ == '__main__':
    main()