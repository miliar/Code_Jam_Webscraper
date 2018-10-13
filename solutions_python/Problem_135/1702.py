t = int(raw_input())
for test in range(1,t+1):
    row = [[],[],[],[]]
    nrow = [[],[],[],[]]
    x=int(raw_input())
    for i in range(4):
        row[i] = map(int,raw_input().split(' '))
    y=int(raw_input())
    for i in range(4):
        nrow[i] = map(int,raw_input().split(' '))
    found = 0
    item = -1
    for i in row[x-1]:
        if i in nrow[y-1]:
            found += 1
            item = i
    if found > 1:
        print 'Case #'+str(test)+': Bad magician!'
    elif found == 1:
        print 'Case #'+str(test)+': '+str(item)
    else:
        print 'Case #'+str(test)+': Volunteer cheated!'
