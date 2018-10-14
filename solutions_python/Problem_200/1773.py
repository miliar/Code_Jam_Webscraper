
def solve(n):
    list_nums = [long(x) for x in n]

    last_digit = -1
    for i, num in enumerate(list_nums):
        if num < last_digit:
            while i > 0 and list_nums[i] < list_nums[i-1]:
                list_nums[i-1] -= 1
                i -= 1

            list_nums[i+1:] = [9 for x in range(len(list_nums) - (i+1))]
            break

        last_digit = num

    return long("".join([str(x) for x in list_nums]))


def main():
    num_cases = int(raw_input())

    for case_index in range(num_cases):
        case_line = raw_input()
        n = case_line

        answer = solve(n)

        print("Case #{}: {}".format(case_index+1, answer))

main()
