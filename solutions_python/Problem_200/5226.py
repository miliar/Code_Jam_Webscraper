from sys import stdin


def solve(input):
    val = int(input)
    val_s = input.strip()
    while True:
        if val < 10:
            return val

        tidy = True
        for first, second in zip(val_s[:-1], val_s[1:]):
            if first > second:
                tidy = False
                break
        if tidy:
            return val

        max_digit = 0
        max_digit_ind = 0
        for i in xrange(len(val_s) - 1, -1, -1):
            int_i = int(val_s[i])
            if int_i >= max_digit:
                max_digit = int_i
                max_digit_ind = i

        to_subtract = (int(val_s[min(max_digit_ind + 1, len(val_s) - 1):]) + 1)
        val -= to_subtract
        val_s = str(val)



if __name__ == '__main__':
    cases = int(stdin.readline())
    cnt = 1
    while cases:
        result = solve(stdin.readline())
        print 'Case #%d: %d' % (cnt, result)
        cnt += 1
        cases -= 1
