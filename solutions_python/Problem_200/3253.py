def validator(s):
    return all([
        True if int(s[idx]) <= int(s[idx + 1]) else False for idx in range(0, len(s) - 1)
    ])


def mm(s):
    output = []
    carry = False
    for idx in range(0, len(s) - 1):
        if carry:
            output.append('9')
        elif int(s[idx]) > int(s[idx + 1]):
            output.append(str(int(s[idx]) - 1))
            carry = True
        else:
            output.append(s[idx])

    if carry:
        output.append('9')
    else:
        output.append(s[-1])
    return ''.join(output).lstrip('0')


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    s = input()

    while not validator(s):
        s = mm(s)
    print("Case #{}: {}".format(i, s))
    # check out .format's specification for more formatting options
