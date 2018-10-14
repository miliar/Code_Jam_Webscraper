def debug(msg):
    #print(msg)
    pass

def tidy_number(digits):
    debug("digits is {0}".format(digits))

    last = len(digits) - 1
    for i in range(last, 0, -1):
        if digits[i - 1] > digits[i]:
            debug("fixing number {0}".format(digits))
            digits[i - 1]  = digits[i - 1] - 1
            digits[i]  = 9

            k = i + 1
            while k < len(digits):
                digits[k] = 9
                k += 1

            return tidy_number(digits)

    return digits

def tidy():
    t = int(input())
    for case in range(1, t + 1):
        n = int(input())

        debug("number was: {0}".format(n))
        digits = [int(x) for x in str(n)]
        soln = int("".join(str(x) for x in tidy_number(digits)))
        print("Case #{0}: {1}".format(case, soln))

        # slow solution
        #last_tidy = 0
        #last_number = n
        #while last_number >= 0:
        #    if tidy_number(last_number):
        #        print("Case #{0}: {1}".format(case, last_number))
        #        break
        #    last_number -= 1


if __name__ == '__main__':
    tidy()
