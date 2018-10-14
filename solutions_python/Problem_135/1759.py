file=open("A-small-attempt1.in","r")
count=int(file.readline()[:-1])
for m in range (count):
    guess1=int(file.readline()[:-1])
    for x in range (guess1):
        array1=file.readline()[:-1].split(" ")
    for x in range (4-guess1):
        dummy=file.readline()[:-1].split(" ")
    guess2=int(file.readline()[:-1])
    for x in range (guess2):
        array2=file.readline()[:-1].split(" ")
    for x in range (4-guess2):
        dummy=file.readline()[:-1].split(" ")
    count=0;
    ans=0;
    for x in array1:
        if x in array2:
            count+=1
            ans=int(x)
    if(count>1):
        print("Case #"+str(m+1)+": "+"Bad magician!")
    elif(count==1):
        print("Case #"+str(m+1)+": "+str(ans))
    else:
        print("Case #"+str(m+1)+": "+"Volunteer cheated!")

        
    
