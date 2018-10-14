t = int(input())

for i in range(1, t+1):
    n = input()


    tidy = False
    while not tidy:
        num = []           
        for item in range(len(n)):
            num.append(int(n[item]))

        change = False        
        for j in range(len(num)-1):
            if num[j]>num[j+1]:
                num[j] -= 1
                bad = j+1
                change = True
                break

        if change:
            for k in range(bad, len(num)):
                num[k] = 9

            if num[0] == 0:
                num.pop(0)

        tidy = True
        for j in range(len(num)-1):
            if num[j]>num[j+1]:
                tidy = False

        n = ''
        for k in range(len(num)):
            n += str(num[k])

    print("Case #{}: {}".format(i, n))
