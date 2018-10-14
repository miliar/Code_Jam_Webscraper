def get_problem_digit(num):
    """
        problem digit - first non increasing digit
        return a tuple with a success boolean and index integer value
        (True, index) - a problem digit was found at index
        (False, None) - No problem digit was found
    """
    chars = str(num)
    for i in range(len(chars) - 1):
        current_digit = int(chars[i])
        next_digit = int(chars[i + 1])
        if current_digit > next_digit:
            return True, i + 1
    return False, None


def last_tidy(num):

    success, index = get_problem_digit(num)
    if not success:
        return num

    digits = list(str(num))

    for i in reversed(range(0, index)):
        current_digit = int(digits[i])
        previous_digit = int(digits[i - 1]) if i > 0 else None
        if previous_digit is None or current_digit - 1 >= previous_digit:
            digits[i] = str(current_digit - 1)
            for j in range(i + 1, len(digits)):
                digits[j] = '9'
            break

    return int("".join(digits))

cases = int(input())
for case in range(1, cases + 1):
    n = int(input())
    print("Case #{}: {}".format(case, last_tidy(n)))
"""
find the first non increasing term,
reduce the first reducable number before it
and then flip the rest to 9s

N       MY RESULT  CORRECT RESULT
10      09          9
101     099         99
1000    0999        999
1100    0999        999
1120    1119        1119
1220    1199        1199
1232    1229        1229
132     129         129
7       7           7
1110    0999
"""

