cases = int(input())

all_cases = []

for i in range(cases):
    test_case = int(input())
    all_cases.append(test_case)


def make_tidy(num):
    i = 1
    while num // exp(i) > 0:
        first_index = (num % exp(i)) // exp(i-1)
        second_index = (num % exp(i+1)) // exp(i)
        if second_index > first_index:
            final_int = 0
            for j in range(i):
                final_int += 9*exp(j)
            final_int += (num // exp(i) - 1) * exp(i)
            num = final_int
        i+=1
    return num


def exp(num):
    return 10 ** num

def int_len(num):
    num = abs(num)
    if num < 10:
        return 1
    return 1 + int_len(num / 10)


for i in range(len(all_cases)):
    print("Case #{}: {}".format(i + 1, make_tidy(all_cases[i])))