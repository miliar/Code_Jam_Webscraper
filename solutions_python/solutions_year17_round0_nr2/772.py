import sys


#cin = open('input.txt', 'r')
#cin = open('B-small-attempt0.in', 'r')
cin = open('B-large.in', 'r')
#cin = sys.stdin
cout = open('output.txt', 'w')
#cout = sys.stdout

current_str_iter = None


def next_token():
    global current_str_iter

    while True:
        if current_str_iter is not None:
            token = next(current_str_iter, None)
            if token is not None:
                return token

        current_str_iter = iter(cin.readline().split())


def next_int():
    return int(next_token())


def solve(number):
    number = list(number)
    remnant = False
    reset_from = len(number)

    for i in range(len(number) - 1, -1, -1):
        if remnant:
            remnant = False
            number[i] = chr(ord(number[i]) - 1)

        if i > 0 and ord(number[i]) < ord(number[i - 1]):
            reset_from = i
            remnant = True

    for i in range(reset_from, len(number)):
        number[i] = '9'

    return int(''.join(number))


def main():
    testcases = next_int()

    for tc in range(1, testcases + 1):
        number = next_token()

        result = solve(number)

        cout.write('Case #%i: %s\n' % (tc, str(result)))


if __name__ == '__main__':
    main()