def readInItems(filename):
    read_data = None;
    with open(filename, 'r') as f:
       read_data = f.read()
    f.close()

    return read_data



xname ='C:\\Users\\Red Lion\\Desktop\\test.in'

x = readInItems(xname)
x = x.split("\n")
#print(x)

cases = int(x[0])
#print(cases)
for s in range(cases):
    #print(x[s+1])
    parts = x[s+1].split(" ")
    #print(parts)
    smax = parts[0]
    audience = parts[1]
    #print(smax)
    #print(audience)
    friends = 0
    counter = 0
    added = 0
    while(counter <= int(smax)):
        p = int(audience[counter])
        if(friends >= counter):
                pass
        elif(friends < counter):
                add = counter-friends
                added = add + added
                friends = friends + add

        friends = friends + p
        counter = counter + 1

    print("Case #"+str(s+1)+ ": " + str(added))

    
    
            
        
        
        
    
    

