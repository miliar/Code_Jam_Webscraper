def join_ans(digits):
    n = 0

    for i in digits:
        n = n*10 + i

    return n


def listify(n):
    digits = []

    while n:
        rem = n % 10
        digits.append(rem)
        n //= 10

    return list(reversed(digits))


def update_min_rev_1000(digits):
    for i in reversed(range(1, len(digits))):
        if digits[i] < digits[i-1]:
            digits[i] = 9
            digits[i-1] -= 1

    return join_ans(digits)


def largest_min(digits):
    digits[0] -= 1
    for i in range(1, len(digits)):
        digits[i] = 9

    return join_ans(digits)


def all_digits_same(digits):
    for i in range(len(digits)-1):
        if digits[i] != digits[i+1]:
            return False
    return True


def main():
    inp = open('B-small-attempt2.in', 'r')
    out = open('submit.out', 'w')
    # tc = int(input())
    tc = int(inp.readline())
    for t in range(1, tc+1):
        num = int(inp.readline())
        # num = t
        op = listify(num)

        if len(op) == 1:
            ans = num

        elif len(op) > 1:
            if op[0] > op[1]:
                ans = largest_min(op)
            elif not all_digits_same(op):
                if 1 <= num <= 1000:
                    ans = update_min_rev_1000(op)
            else:
                ans = num

        print("Case #{0}: {1}".format(t, ans), file=out)
        print("file written")
        # print("Case #{0}: {1}".format(t, ans))


if __name__ == '__main__':
    main()
