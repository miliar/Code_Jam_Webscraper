def t(n):
    if n == 1:
        return 1
    else:
        return 2*t(n-1) + 1 

for case in range(int(input())):
    n,k = map(int, input().split())

    turnon = t(n)

    if k % (turnon+1) == turnon and k > 0:
        print("Case #" + str(case+1) + ": ON")
    else:
        print("Case #" + str(case+1) + ": OFF")
