import sys

def get_nearest_tidy(n):

    # get digits list for number
    digits = [int(d) for d in str(n)]

    if len(digits) < 2:
        return n

    tidy_number = 0

    # compare consecutive two digits from digits
    # if left one is greater then in right digit then
    # number n is not tidy number
    for i, (ld, rd) in enumerate(zip(digits, digits[1:])):
        if ld > rd:

            # reduce digit by 1
            digits[i] = digits[i] - 1

            # for rest of the digits convert it in 9
            for x in range(i + 1, len(digits)):
                digits[x] = 9

            # recursive call for this new number
            tidy_number = int("".join(str(x) for x in digits))
            return get_nearest_tidy(tidy_number)

    return n

# ==============
# MAIN PROGRAM
# ==============

# get input file
input_file = sys.stdin

# skip first line
T = next(input_file)

# 1<= T <= 100
if int(T) > 100 and int(T) < 0:
    sys.exit(0)

# proceed operation for further numbers from file
for index, line in enumerate(input_file, 1):

    # if test cases
    if index > int(T):
        sys.exit(0)

    num = line.strip()

    if not num:
        continue

    # get nearest closest tidy number
    n = get_nearest_tidy(int(num))
    print "Case #{}: {}".format(index, n)

sys.exit(0)
