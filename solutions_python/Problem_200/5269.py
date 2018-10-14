'''t=int(input())
def readNumber(times):
    n=int(input())
    counter=n
    while True:
        myList=[]
        count=0
        for i in str(counter):
            myList.append(int(i))
        for i in range(len(myList)-1):
            if myList[i]<=myList[i+1]:
                count+=1
            else:
                break
        if count==len(myList)-1:
            print ("Case #"+str(times+1)+": "+str(counter))
            break
        counter-=1
for i in range(t):
    readNumber(i)
'''
f=open("B-small-attempt2.in")
g=open("output-file.txt","a")
t=int(f.readline())
#t=int(input())
def readNumber(times):
    #n=int(input())
    n=int(f.readline())
    counter=n
    while True:
        myList=[]
        count=0
        for i in str(counter):
            myList.append(int(i))
        for i in range(len(myList)-1):
            if myList[i]<=myList[i+1]:
                count+=1
            else:
                break
        if count==len(myList)-1:
            print ("Case #"+str(times+1)+": "+str(counter))
            g.write("Case #"+str(times+1)+": "+str(counter)+"\n")
            break
        counter-=1
for i in range(t):
    readNumber(i)
f.close()
g.close()
