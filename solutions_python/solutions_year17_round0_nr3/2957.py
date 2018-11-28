def main():
    numCases = int(input());
    for test in range(1, numCases + 1):
        m, n = [int(s) for s in input().split(" ")]
        bathroom = [0] * m
        for t in range(0, n-1):
            d, e, f = position(bathroom) #index, ls, rs
            bathroom[d] = 1
        d, e, f = position(bathroom)
        bathroom[d] = 1
        print("Case #" + str(test) + ": " + str(max(e,f)) + " " + str(min(e,f)))

def position(list):
    countoccupied = 0  # number occupied
    occupied = []  # indices in list[] of occupied bathrooms
    for x in range(0, len(list)): #cycling through list[] to find occupied bathroom
        if(list[x] == 1):
            occupied.append(x)
            countoccupied += 1
    ls = [0]*len(list)
    rs = [0]*len(list)
    #fill ls
    for x in range(1, len(list)): #goes through each bathroom stall
        for a in range(x, -1, -1):
            if(list[a] == 1):
                ls[x] = x - (a+1)
                break
            elif(a == 0):
                ls[x] = x
    #fill rs
    for y in range(0, len(list)-1): #goes through each bathroom stall
        for b in range(y, len(list)):
            if(list[b] == 1):
                rs[y] = b - (y+1)
                break
            elif(b == len(list)-1):
                rs[y] = len(list) - 1 - y
    #check stuff
    minimum = -2
    location = []
    for z in range(0, len(list)):
        if(list[z] != 1 and min(ls[z], rs[z]) > minimum):
            minimum = min(ls[z], rs[z])
            location = [z]
        elif(list[z] != 1 and min(ls[z], rs[z]) == minimum):
            location.append(z)
    if(len(location) == 1):
        return location[0], ls[location[0]], rs[location[0]]
    maximum = max(ls[location[0]], rs[location[0]])
    counter = 1
    location2 = location[0]
    for a in range(1, len(location)):
        if(max(ls[location[a]], rs[location[a]]) > maximum):
            location2 = location[a]
            maximum = max(ls[location[a]], rs[location[a]])
            counter = 1
        elif(max(ls[location[a]], rs[location[a]]) == maximum):
            counter += 1
    return location2, ls[location2], rs[location2]

main()