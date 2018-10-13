list_node1=[]
list_node2=[]
file=open("A-small-attempt2.in","r")
#outfile=open("dilanka.txt","w")
testcase=file.readline()
count=0
i=0
j=0
def search(node1,node2,u):
    counter=0
    list1=[]
    for i in range(0,4):
        l=node1[int(row1)-1][i]
        for j in range(0,4):
            m=node2[int(row2)-1][j]
            if(l==m):
                list1.append(l)
            else:
                counter=counter+1                

    if(len(list1)==1):
        print("Case #"+str(u)+": " +list1[0])
        #outfile.write("Case #"+str(u)+": " +list1[0]+"\n")
        
    elif(counter==16):
        print("Case #"+str(u)+": " +"Volunteer cheated!")
        #outfile.write("Case #"+str(u)+": " +"Volunteer cheated!"+"\n")
        
    else:
        print("Case #"+str(u)+": " +"Bad magician!")
        #outfile.write("Case #"+str(u)+": " +"Bad magician!"+"\n")
        
u=0
while(count<int(testcase)):
    row1 = file.readline()
    while(i<4):
        list_node1.append((file.readline().split()))
        i=i+1  
    i=0
    row2 = file.readline()
    while(j<4):
        list_node2.append((file.readline().split()))
        j=j+1
    count=count+1
    u=u+1
    j=0
    search(list_node1,list_node2,u)
    list_node1=[]
    list_node2=[]







    
