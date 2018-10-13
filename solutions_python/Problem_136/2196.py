from sys import stdin

def cookie(C,F,X):
    prod = 2

    old_time = X/prod
    new_time = C/prod + X/(prod+F)

    time, cur_time = C/prod, 0
    while new_time < old_time:
        old_time = new_time
        prod += F

        time += C/prod
        cur_time = time + X/(prod+F)
        new_time = cur_time

    return old_time

t = int(stdin.readline())
for kase in range(t):
    C,F,X = map(float,stdin.readline().split())
    print("Case #%d: %.7f" %(kase+1,cookie(C,F,X)))