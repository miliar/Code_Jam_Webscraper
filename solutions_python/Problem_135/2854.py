loops = input().strip()
loops = int(loops)
i = 1
while(i <= loops):
    line = int(input().strip())-1
    array = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    j=0
    
    while (j<4):
        temp=input().strip().split()
        k=0
        while(k<4):
            array[j][k] = int(temp[k])
            k+=1
        j+=1

    line2 = int(input().strip())-1
    array2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    j=0
    
    while (j<4):
        temp=input().strip().split()
        k=0
        while(k<4):
            array2[j][k] = int(temp[k])
            k+=1
        j+=1

    answer =0
    for x in array[line]:
        for y in array2[line2]:
            if (x==y):
                if(answer==0):
                    answer = x
                else:
                    answer = -1

    if(answer == -1):                
        print("Case #" + str(i) + ": " + "Bad magician!")
    elif(answer == 0):
        print("Case #" + str(i) + ": " + "Volunteer cheated!")
    else:
        print("Case #" + str(i) + ": " + str(answer))
     
    i+=1
