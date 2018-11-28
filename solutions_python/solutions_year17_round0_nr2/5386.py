cases = [int(input()) for _ in range(input())]

for index, case in enumerate(cases):
    max_tidy = 0
    for num in range(case + 1):
        if "".join(sorted(str(num))) == str(num):
            max_tidy = num
    print("Case #{}: {}".format(index + 1, max_tidy))