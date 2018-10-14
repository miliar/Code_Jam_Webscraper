def counter(n):
    for i in range(int(n), 0 , -1):
        max_digit = 0
        is_tidy = True
        for d in str(i):
            if int(d) < max_digit:
                is_tidy = False
                break
            max_digit = int(d)
        if is_tidy:
            return i



n = int(input())

for i in range(1, n + 1):
    t = input()
    print("Case #{}: {}".format(i, counter(t)))
