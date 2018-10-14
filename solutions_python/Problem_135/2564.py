f = open('D:/A-small-attempt0.in', 'r')
T = int(f.readline().strip())
for j in range(T):
    first = int(f.readline().strip())
    row = list()
    for i in range(4):
        row.append(f.readline().strip().split(" "))
    row = row[first-1]
    second = int(f.readline().strip())
    row2 = list()
    for i in range(4):
        row2.append(f.readline().strip().split(" "))
    row2 = row2[second-1]
    counter = 0
    value = 0
    for x in row:
        if x in row2:
            counter+=1
            value = x
    if counter > 1:
        print("Case #"+str(j+1)+": Bad magician!")
    if counter == 1:
        print("Case #"+str(j+1)+": "+value)
    if counter == 0:
        print("Case #"+str(j+1)+": Volunteer cheated!")