d = open('A-large.in').readlines()

i = 1
while i < int(d[0]) + 1:
    people = d[i].split(" ")[1]
    shyness = 0
    friends = 0
    totalPeople = 0
    for num in people:
    
        try:
            num = int(num)
            if (num == 0):
                pass
            elif (totalPeople >= shyness):
                totalPeople += num
            else:
                while (totalPeople < shyness):
                    totalPeople += 1
                    friends     += 1
                totalPeople += num
                
        except:
            break
        shyness += 1
    print("Case #{0}: {1}".format(i, friends))
    i += 1
        
