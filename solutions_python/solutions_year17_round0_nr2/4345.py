
def calculate_tidynumber(n):
    str_n = str(n)
    sorted_str_n = "".join(sorted(str_n))
    count = 1
    while str_n != sorted_str_n:
        n = n - ((n % (10**count)) + 1)
        str_n = str(n)
        count += 1
        sorted_str_n = "".join(sorted(str_n))
    return n

t = int(input())

for i in range(1, t + 1):
    n = int(input())
    tidy_number = calculate_tidynumber(n)
    print("Case #{}: {}".format(i, tidy_number))
