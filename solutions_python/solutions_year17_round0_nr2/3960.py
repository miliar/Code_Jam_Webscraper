def is_tidy(number):
    num_text = str(number)
    for index in range(0, len(num_text)-1):
        if num_text[index] > num_text[index+1]:
            return False
    return True


def find_tidy(number):
    for num in range(number, 1, -1):
        if is_tidy(num):
            return num
    return 1


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())

    print("Case #{}: {}".format(i, find_tidy(n)))

