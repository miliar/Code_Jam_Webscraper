
TCASE = int(input())

def is_tidy_num(num):
    before = num%10
    if before == 0:
        return False
    num = int(num/10)
    while num > 0:
        if before < num%10:
            return False
        before = num%10
        num = int(num/10)

    return True

checked = [False]*1001

for i in range(1, 1001):
    checked[i] = is_tidy_num(i)

for i in range(1,TCASE+1):
    N = int(input())
    while not checked[N]:
        N -= 1

    print('Case #{}: {}'.format(i, N))
