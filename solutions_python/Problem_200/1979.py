def solve(n):
    while not is_tidy(n):
        n = clean(n)
    return n


def clean(n):
    n_inv = n[::-1]
    len_n_inv = len(n_inv)
    for i in range(len_n_inv - 1):
        if int(n_inv[i]) < int(n_inv[i + 1]):
            return str(int(str(int(n[:len_n_inv - i]) - 1) + '9' * i))


def is_tidy(n):
    len_n = len(n)
    for i in range(len_n):
        if i != (len_n - 1) and int(n[i]) > int(n[i + 1]):
            return False
    return True


t = int(input())
for i in range(1, t + 1):
    print("Case #{}: {}".format(i, solve(str(input()))))
