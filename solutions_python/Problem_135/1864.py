import os
outfile = open(r'C:\Users\PK GUPTA\Downloads\A-small-out.txt', 'w')
fi=[]
count=0

with open(r'C:\Users\PK GUPTA\Downloads\A-small-attempt0.in') as f:
    x=int(f.readline().strip())
    while count!=x:
        lineno1 =f.readline()
        cards1=0
        z1=[]
        #print lineno1
        while cards1!=4:
            content1 = f.readline()
            content1=content1.strip()
            z1.append(content1)
            cards1 =cards1 +1
        #print z1
        lineno2 =f.readline()
        cards2=0
        z2=[]
        #print lineno2
        while cards2!=4:
            content2 = f.readline()
            content2=content2.strip()
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
        count=count+1		
        se= "Case #" + str(count) +": "+w+'\n'
        print se
        outfile.write(se)

outfile.close()
