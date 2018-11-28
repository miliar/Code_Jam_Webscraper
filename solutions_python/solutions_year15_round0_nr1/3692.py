fd = open("A-small-attempt0.in", 'r')
t_max = int( fd.readline() )
for i in range(t_max):
    total = 0 #how many people are standing
    need = 0  #how many people need to add
    apList = [] #list of people and their shy level
    temp = []
    
    temp = fd.readline().split()
    
    size = int(temp[0])
    temp = temp[1]

    for j in temp:
        apList.append(j)

    for j in range(size+1):
        if( total < j and int(apList[j])>0 ):
            need += j-total
            total += need
        total += int(apList[j])
    print "Case #"+str(i+1)+":", need
        
