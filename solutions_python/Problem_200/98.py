def highest_power_of_10(num):
    power = -1
    while (num != 0):
        num //= 10
        power += 1
    return power


def digit_by_power(num, power):
    return (num // 10 ** (power)) % 10


# first power i from the left that satisfies num[i] < num[i - 1]
# -1 means no descent
def first_power_of_descent_from_left(num):
    power = highest_power_of_10(num)
    for i in range(power, 0, -1):
        if num_descends_at_power(num, i):
            return i
    return -1

def num_descends_at_power(num, power):
    return digit_by_power(num, power) > digit_by_power(num, power - 1)

def fixed(num, descent_power):
    return num // (10 ** descent_power) * (10 ** descent_power) - 1

def largest_tidy_smaller_than(num):
    descent_power = first_power_of_descent_from_left(num)
    if(descent_power == -1):
        return num
    while num_descends_at_power(num, descent_power):
        num = fixed(num, descent_power)
        descent_power += 1
    return num

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    num = int(input())
    print("Case #{}: {}".format(i, largest_tidy_smaller_than(num)))
