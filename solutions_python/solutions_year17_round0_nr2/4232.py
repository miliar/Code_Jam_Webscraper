def get_last_tidy(case):
    n = int(case)
    while not is_tidy(n):
        n -= 1
    return n


def is_tidy(n):
    n = str(n)
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            return False
    return True
