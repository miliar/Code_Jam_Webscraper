# -*- coding: utf-8 -*-

t = int(input())

for i in range(t):
    n = int(input())

    nums = []
    chars = []
    noway = False
    for j in range(n):
        s = input().strip()

        if noway:
            continue

        last = None
        nums.append([])
        chit = -1
        for ch in s:
            if not last or last != ch:
                last = ch
                if j == 0:
                    chars.append(ch)
                else:
                    chit += 1
                    if chit >= len(chars) or ch != chars[chit]:
                        noway = True
                nums[-1].append(1)
            else:
                nums[-1][-1] += 1
        if j != 0:
            if chit != len(chars)-1:
                noway = True

    if noway:
        print("Case #" + str(i+1) + ": Fegla Won")
    else:
        summa = 0
        trans = zip(*nums)
        for col in trans:
            avg = round(sum(col)/len(col))

            for num in col:
                summa += abs(num - avg)

        print("Case #" + str(i+1) + ": " + str(summa))
                
            
            
