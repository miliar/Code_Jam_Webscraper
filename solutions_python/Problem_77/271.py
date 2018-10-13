incoming=open('D-large.in','r')
a=int(incoming.readline())
f=open('D-large-output.txt','w')

for i in range(1,a+1):
    total=int(incoming.readline())
    numbers=incoming.readline().split()
    
    mess = 0

    for (element,index) in zip(numbers,range(1,total+1)):
        test = int(element)
        if test != index:
            mess+=1

    f.write("Case #"+str(i)+": "+str(mess)+".000000\n")
f.close()
incoming.close()
