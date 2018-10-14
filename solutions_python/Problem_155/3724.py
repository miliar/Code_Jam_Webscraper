T = int(input())
cas = 1

while cas <= T:
    data = input().split()
    smax = int(data[0])
    audien = [int(i) for i in data[1]]

    friend_number = 0
    stod = 0

    for i in range(len(audien)):
        if (stod < i) and audien[i]:
            friend_number += i - stod
            stod += friend_number
        stod += audien[i]

    print("Case #"+str(cas)+":", friend_number)

    cas += 1
