from decimal import Decimal
finput = open('testInput.in', 'r')
foutput=open('optest1.in','w')
str=finput.readline()
counter=0
while(str):
    row=int(finput.readline())
    print "row",row
    array=[]
    for i in range(4):
        str=finput.readline()
        if(i+1==row):
            list1=str.split(' ')
        lst=str.split(' ')
        array.append(i)
        
    row=int(finput.readline())
    array=[]
    for i in range(4):
        str=finput.readline()
        if(i+1==row):
            list2=str.split(' ')
        lst=str.split(' ')
        array.append(i)
    number=[]  
    print "list1",list1
    print "list2",list2  
    for i in range(4):
        list1[i]=list1[i].rstrip()
        list2[i]=list2[i].rstrip()
    for i in range(4):
        if (list1[i] in list2):
            number.append(list1[i])
    print "number is",number        
    if(len(number)==1):        
        foutput.write("Case #%d: %s\n"%(counter+1,number[0]))
    elif(len(number)>1):
        foutput.write("Case #%d: Bad magician!\n"%(counter+1))
    elif(len(number)==0):
        foutput.write("Case #%d: Volunteer cheated!\n"%(counter+1))
    
    counter+=1
    print "*****************************************"
    
            
    
    
    