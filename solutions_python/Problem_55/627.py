def printResult(case, r, k, n, groups):
    coaster = []
    money = 0
    for i in range(r):
        #Board the coaster
        while len(groups) > 0:
            nextgroup = groups.pop(0)
            if sum(coaster) + nextgroup <= k:
                coaster.append(nextgroup)
            else:
                groups.insert(0, nextgroup)
                break

        #Ride!
        money += sum(coaster)

        #Get off the coaster
        while len(coaster) > 0:
            groups.append(coaster.pop(0))

    print("Case #%i: %d" % (case, money))

for i in range(int(raw_input())):
    r,k,n = map(lambda x: int(x), raw_input().split())
    groups = map(lambda x: int(x), raw_input().split())
    printResult(i+1, r, k, n, groups)
