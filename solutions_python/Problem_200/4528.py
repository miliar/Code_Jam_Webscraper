def is_sorted_string(str):
    for i in range(len(str) - 1):
        if str[i] > str[i + 1]:
            return False
    return True


def tidy_number(n):
    if len(str(n)) == 1:
        return n

    if is_sorted_string(str(n)):
        return n

    while n > 0:
        n = n - 1
        if is_sorted_string(str(n)):
            return n

    return n


output = open('output.in', 'w')


t = int(input())  # read a line with a single integer

for i in range(1, t + 1):
    n = int(input())
    print("Case #{}: {}".format(i, tidy_number(n)))
    output.write("Case #{}: {}\n".format(i, tidy_number(n)))
