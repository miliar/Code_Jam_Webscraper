import os
os.getcwd()
os.chdir(r"D:\pratik\code jam\Real Code jam")


myFile = open('magicoutputs.in', 'w')
fi=[]
count=1

with open(r"D:\pratik\code jam\Real Code jam\small.in") as f:
    x=f.readline()
    n=0
    x=int(x)
    
    while n!=x:
        lineno1 =f.readline()
        cards1=0
        z1=[]
        #print lineno1
        while cards1!=4:
            content1 = f.readline()
            content1=content1.strip('\n')
            z1.append(content1)
            cards1 =cards1 +1
        #print z1
        lineno2 =f.readline()
        cards2=0
        z2=[]
        #print lineno2
        while cards2!=4:
            content2 = f.readline()
            content2=content2.strip('\n')
            z2.append(content2)
            cards2 =cards2 +1
        #print z2
        
        l1=z1[int(lineno1)-1]
        l2=z2[int(lineno2)-1]
        l1=l1.split(' ')
        l2=l2.split(' ')
        print l1,l2
        ans=[]
        for i in l1:
            if i in l2:
                print i
                ans.append(i)
            else:
                pass
        print ans
        if len(ans)==1:
            w=ans[0]
        elif len(ans)==0:
            w='Volunteer cheated!'
        else:
            w='Bad magician!'
        count=str(count)
        se= "Case #" + count +": "+w+'\n'
        print se
        myFile.write(se)
        count=int(count)
        count=count+1
        n=n+1

myFile.close()