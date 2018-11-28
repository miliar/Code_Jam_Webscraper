#park.py
#Run on Python 2.6.5

fileName = raw_input("Enter the input filename:")
f_in = open(fileName,'r')
f_out = open('OUT-'+fileName,'w')

T = int(f_in.readline())

for C in range(T):
    
    RkN = f_in.readline().split(' ')
    R, k, N = int(RkN[0]), int(RkN[1]), int(RkN[2])
    
    groups = f_in.readline().split(' ')
    for i in range(len(groups)):
        groups[i] = int(groups[i])
    
    money = 0 #The cumulative amount of money made
    i = 0 #The index for traversing the group list
    load = 0    
    group_loaded = 0 #The number of groups that has been loaded onto the ride
    
    for r in range(R):
    
        load = 0 #The current number of people in the roller coaster
        group_loaded = 0 
        
        while (load + groups[i]) <= k and group_loaded < N:
            load = load + groups[i]
            money = money + groups[i]
            group_loaded = group_loaded + 1
            i = (i + 1) % N #Cycle through the group list if i has reached the end
            
     
    f_out.write("Case #{0}: ".format(C+1) + str(money) +'\n')
    
    
       
print "Solved"   
f_in.close()
f_out.close()