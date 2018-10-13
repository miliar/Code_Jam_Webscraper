import math

def is_square(num):
    if num == 1: return True

    x = num // 2
    seen = set([x])
    while x * x != num:
        x = (x + (num // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True

def number_of_palin(lower, upper):
    num_of_palindrom = 0

    for i in range(lower, upper+1):
        if is_square(i):
            i_str = str(i)
            i_sqrt_str = str(int(math.sqrt(i)))
            if i_str == i_str[::-1] and i_sqrt_str == i_sqrt_str[::-1] :
                num_of_palindrom += 1

    return num_of_palindrom


if __name__ == '__main__':
    num_of_test_cases = int(input())
    for i in range(num_of_test_cases):
        l, u = [ int(i) for i in input().strip().split() ]
        print("Case #{}: {}".format(i+1, number_of_palin(l, u)))