def check_tidy(x):
    x = str(x)
    cur = x[0]
    for i in range(1, len(x)):
        if (x[i] >= cur):
            cur = x[i]
        else:
            return False
    return True

def last_tidy(x):
    while not check_tidy(x):
        x -= 1
    return x

t = int(input())
for n in range(t):
    print("Case #{}: ".format(n+1), end='')
    print(last_tidy(int(input())))
