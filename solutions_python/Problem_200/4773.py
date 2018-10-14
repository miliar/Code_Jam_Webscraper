T = int(input())
def is_tidy(x):
    x = str(x)
    for i in range(len(x) - 1):
        if int(x[i + 1]) < int(x[i]):
            return False
    return True
for t in range(T):
    n = int(input())
    while not is_tidy(n):
        n -= 1
    print('Case #{}: {}'.format(t + 1, n))
