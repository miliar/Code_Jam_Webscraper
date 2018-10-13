'''
Created on 2013/5/12

@author: kaimugen
'''
f=open("A-small-attempt0.in",'r')
f2=open("output.txt",'w')
caseConnt=int(f.readline())
case=0
while(case<caseConnt):
    case=case+1
    line=f.readline()
    line=line[:-1]
    temp=line.split(' ')
    
    vowel=['a','e','i','o','u']
    rootList=[]
    rootS=[]
    rootN=[]
    for i in range(0,len(temp[0])-int(temp[1])+1):
        root=''
        check=True
        for w in range(i,int(temp[1])+i):
            if(temp[0][w] not in vowel):                
                root=root+temp[0][w]
            else:
                check=False
                break
        #print(root)
        if check:
            #rootList.append(root)
            rootS.append(i)
            rootN.append(int(temp[1])+i-1)
    sum=0
    for i in range(len(rootS)):
        if(i==0):
            sum=sum+((rootS[i]+1)*(len(temp[0])-rootN[i]))
        else:
            sum=sum+((rootS[i]-(rootS[i-1]+1)+1)*(len(temp[0])-rootN[i]))
    f2.write("Case #%d: %d\n"%(case,sum))
f.close()
f2.close()