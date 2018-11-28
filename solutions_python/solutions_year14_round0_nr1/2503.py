maincount = 0
f = open('A-small-attempt3.in', 'r')
cases = int(f.readline())
for y in range(0,cases):

    oneps = int(f.readline())

    lineOne=[]
    for i in range(0,4):
        lineOne.append((f.readline()[:-1]).split(" "))
         

    twops = int(f.readline())

    lineTwo = []
    for i in range(0,4):
        lineTwo.append((f.readline()[:-1]).split(" "))
        

    s = []
    count=0
    for x in lineOne[oneps-1]:
        if x in lineTwo[twops-1]:
            count = count+1
            s.append(x)


    if(count==1):
        print("Case #"+str(y+1)+": "+s[0])
    elif(count>1):
        print("Case #"+str(y+1)+": "+"Bad magician!")
    else:
        print("Case #"+str(y+1)+": "+"Volunteer cheated!")
            
        

