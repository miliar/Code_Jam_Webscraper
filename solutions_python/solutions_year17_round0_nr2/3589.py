cases = int(input())


def is_tidy(num):
    num = list(num)
    for x in range(0, len(num) - 1):
        if num[x] > num[x+1]:
            return False
    return True

for case in range(0, cases):
    nums = input()

    for i in range(int(nums), 0, -1):
        if is_tidy(str(i)):
            print('Case #{}: {}'.format(case + 1, str(i)))
            break
