t = int(input())

for i in range(0, t):
    n = input()
    n_int = int(n)


    while(True):
        found = True
        for j in range(0, len(n) - 1):
            if n[j] > n[j+1]:
                found = False
                break

        if found:
            break

        n_int -= 1
        n = str(n_int)

    print('Case #'+str(i+1) +': '+n)