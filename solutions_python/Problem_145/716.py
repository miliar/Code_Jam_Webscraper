import fileinput
file = fileinput.input()


def gcd(m, n):
    if (n <= 0):
        return m
    else:
        return gcd(n, m % n)


num_case = int(file.readline())
for ith_case in range(num_case):
    P, Q = tuple(map(int, file.readline().strip().split('/')))
    f = gcd(Q, P)
    P, Q = P//f, Q//f
    match = False
    for e in range(32):
        if Q == pow(2, e):
            match = True
            break
    if match is not True:
        print("Case #{}: {}".format(ith_case+1, "impossible"))
        continue
    for i in range(32):
        if P*pow(2, i) >= Q:
            print("Case #{}: {}".format(ith_case+1, i))
            break
