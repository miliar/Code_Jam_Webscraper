def gcd(a, b):
    c = 1;
    while a > 0 and b > 0:
        if a % 2 == 0 and b % 2 == 0:
            a = a / 2;
            b = b / 2;
            c = c * 2;
        if a % 2 == 0 and b % 2 == 1:
            a = a / 2;
        if a % 2 == 1 and b % 2 == 0:
            b = b / 2;
        if a % 2 == 1 and b % 2 == 1:
            if a > b:
                a = a % b;
            else:
                b = b % a;
    return c * (a + b)


test = int(raw_input())

for itest in range(1, test + 1):
    line = raw_input()
    temp = line.split(' ')
    n = int(temp[0])
    a = []
    for i in range(1, n + 1):
        a.append(int(temp[i]))

    a.sort()
     
    uc = a[1] - a[0];
    for i in range(2, n):
        uc = gcd(uc, a[i] - a[i - 1])
    res = a[0] % uc
    if res != 0:
        res = -(res - uc)
    print "Case #" + str(itest) + ": " + str(res)
