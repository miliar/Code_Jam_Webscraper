t = int(input())  # read a line with a single integer

for j in range(1, t + 1):
    s, k = input().split(" ")
    k = int(k)

    if k == 1:
        print("Case #{}: {}".format(j, s.count('-')))
        continue

    cnt = 0
    l = len(s)

    flips = []

    for i in s[:-k+1]:  # when k = 1, this gives [:0] which is bad -- so we make that a special case above
        flips = [x-1 for x in flips]

        if len(flips) > 0 and flips[0] == 0:
            flips = flips[1:]

        #print(i, flips, cnt)
        if i == '+':
            if len(flips)%2 == 0:
                continue
            else:
                cnt += 1
                flips.append(k)

        elif i == '-':
            if len(flips)%2 == 1:
                continue
            else:
                cnt += 1
                flips.append(k)



    #print('stage 2')

    for i in s[l-k+1:]:
        flips = [x-1 for x in flips]

        if len(flips) > 0 and flips[0] == 0:
            flips = flips[1:]


        #print(i, flips, cnt)
        if i == '+':
            if len(flips)%2 == 0:
                continue
            else:
                cnt = 'IMPOSSIBLE'
                break

        elif i == '-':
            if len(flips)%2 == 1:
                continue
            else:
                cnt = 'IMPOSSIBLE'
                break

  
    print("Case #{}: {}".format(j, cnt))