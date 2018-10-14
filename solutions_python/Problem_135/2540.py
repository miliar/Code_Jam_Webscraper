'''
Created on 12-Apr-2014

@author: karthik
'''
i=0
f=open('A-small-attempt0.in','r')
tests=f.readline()
a=open('output.txt','w') 
while(i<tests):
    count=0
    chance1=int(f.readline())
    row1=[[]]
    row1.append(f.readline().split())
    row1.append(f.readline().split())
    row1.append(f.readline().split())
    row1.append(f.readline().split())
    chance2=int(f.readline())
    ro1=[[]]
    ro1.append(f.readline().split())
    ro1.append(f.readline().split())
    ro1.append(f.readline().split())
    ro1.append(f.readline().split())
    for x in row1[chance1]:
        for y in ro1[chance2]:
            if(x==y):
                count+=1
                ans=x
    
               
    if(count==0):
        a.write("Case #%s: Volunteer cheated!\n"%(i+1))
    if(count==1):
        a.write("Case #%s: %s\n"%(i+1,ans))
    if(count>1):
        a.write("Case #%s: Bad magician!\n"%(i+1))

    i+=1
    
    

if __name__ == '__main__':
    pass