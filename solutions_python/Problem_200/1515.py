def is_tidy(n):
    prev = 10
    while n > 0:
        digit = n % 10
        if digit > prev: return False
        n //= 10
        prev = digit
    return True

def last_tidy(n):
    if is_tidy(n): return n
    else:
        l = list(str(n))
        max_i = l.index(max(l))
        l[max_i] = str(int(l[max_i]) - 1)
        for i in range(max_i + 1, len(l)):
            l[i] = "9"
        return last_tidy(int("".join(l)))

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    print("Case #{}: {}".format(i, last_tidy(n)))
