# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def recurse(number, i, last, num_len):
    if i >= num_len:
        return 0
    if number[i] < last:
        return -1

    next = recurse(number, i + 1, number[i], num_len)
    if next < 0:
        if number[i] > last:
            next = 10 ** (num_len-i-1) - 1
            number[i] -= 1
        else:
            return -1

    return next + number[i] * 10 ** (num_len-i-1)




t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    str_number = input()
    number = []
    for j in range(len(str_number)):
        number.append(int(str_number[j]))
    tidy = recurse(number, 0, 0, len(number))
    print("Case #{}: {}".format(i, tidy))
