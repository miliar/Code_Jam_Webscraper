def solve(test_num):
    num_str = input().strip()
    num = list(num_str)

    idx = 0
    while idx + 1 < len(num) and num[idx] <= num[idx+1]:
        idx += 1

    # The number is already tidy.
    if idx == len(num) - 1:
        print("Case #{}: {}".format(test_num, num_str))
        return

    for i in range(idx+1, len(num)):
        num[i] = '9'

    while idx - 1 >= 0 and num[idx] == num[idx-1]:
        num[idx] = '9'
        idx -= 1

    # num[idx] > '0'
    num[idx] = chr(ord(num[idx]) - 1)

    print("Case #{}: {}".format(test_num, int("".join(num))))


T = int(input())

for i in range(T):
    solve(i + 1)
