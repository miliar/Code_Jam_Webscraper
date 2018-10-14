#f = open('test.txt', 'r')
f = open('A-large.in', 'r')

cases = int(f.readline())

for case in range(cases):
    intervals = int(f.readline())
    total = 0
    total2 = 0
    tempList = f.readline()
    mush = [int(e) for e in tempList.split(" ")]
    difference = []
    for x in range(len(mush)-1):
        diff = mush[x]-mush[x+1]
        difference.append(diff)
        if diff >= 0:
            total += diff
    for x in range(len(mush)-1):
        if mush[x] <= max(difference):
            total2 += mush[x]
        else:
            total2 += max(difference)

    print("Case #"+str(case+1)+": "+str(total)+" "+str(total2))
        
