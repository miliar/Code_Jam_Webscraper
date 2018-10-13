fi = open("input.txt")
T = int(fi.readline().strip())
for j in (range(T)):
    row = int(fi.readline().strip())
    map=[]
    for i in range(4):
        map.append(fi.readline().strip().split(" "))
    searchRow = set(map[row-1])
    row = int(fi.readline().strip())
    mapp=[]
    for i in range(4):
        mapp.append(fi.readline().strip().split(" "))
    searchRoww = set(mapp[row-1])
    if (len(searchRow - searchRoww) == 3): #found
        print ("Case #" + str(j+1) + ": " + str(searchRow.intersection(searchRoww).pop()))

    elif (len(searchRow - searchRoww) == 4): #found
        print ("Case #" + str(j+1) + ": " + "Volunteer cheated!")

    else:
        print ("Case #" + str(j+1) + ": " + "Bad magician!")
    
        
