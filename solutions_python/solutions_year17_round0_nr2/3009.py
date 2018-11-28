t = int(input())

for k in range(1, t + 1):
    n = input()
    length = len(n)
    if length == 1:
        print('Case #{0}: {1}'.format(k, n))
    elif length >= 2:
        sol = ''.join(['9' for _ in range(length - 1)])
        nex = ''.join(['1' for _ in range(length)])
        n = int(n)
        while int(nex) <= n:
            sol = nex
            if sol == str(n):
                break
            length = len(sol)
            i = length - 1
            while int(nex) <= n:
                sol = nex
                if sol == str(n):
                    break
                if sol[i] != '9':
                    nex = sol[:i] + str(int(sol[i]) + 1) + sol[i+1:]
                else:
                    while i >= 0 and sol[i] == '9':
                        i -= 1
                    if i == -1:
                        break
                    actual = str(int(sol[i]) + 1)
                    nex = sol[:i] + actual + ''.join([actual for _ in range(length - i - 1)])
                    i = length - 1
        print('Case #{0}: {1}'.format(k, sol))

