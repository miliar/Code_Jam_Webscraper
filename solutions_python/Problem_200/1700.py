ORD_ZERO = ord('0')

def last_tidy_pos(num):
    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            return i

    return -1

def is_tidy(num):
    return last_tidy_pos(num) < 0

def last_tidy(num):
    while True:
        lt_pos = last_tidy_pos(num)
        if lt_pos < 0:
            break

        num[lt_pos] -= 1
        for i in range(lt_pos + 1, len(num)):
            num[i] = 9

    return num

def to_bytearray(str_num):
    return bytearray(ord(c) - ORD_ZERO for c in str_num)

def from_bytearray(num):
    return ''.join(chr(i + ORD_ZERO) for i in num).lstrip('0')


def main():
    tests_count = int(input())

    for i in range(1, tests_count + 1):
        str_num = input()
        result = from_bytearray(last_tidy(to_bytearray(str_num)))
        print('Case #{}: {}'.format(i, result))

if __name__ == "__main__":
    main()
