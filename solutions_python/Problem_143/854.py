'''
Created on 03-May-2014

@author: karthik
'''


i=0
f=open('B-small-attempt0.in','r')
tests=int(f.readline())
a=open('output.txt','w') 
for i in range(0,tests):
    count=0
    ilist=[]
    possible=[]
    final=[]
    ilist=f.readline().split()
    for j in range(0,int(ilist[0])):
        for k in range(0,int(ilist[1])):
            possible.append([j,k])
    for l in range(0,len(possible)):
        a=possible[l][0]
        b=possible[l][1]
        final.append(a&b)
    for x in final:
        if(x<int(ilist[2])):
            count+=1
    print "Case #%s: %s"%(i+1,count)
    


if __name__ == '__main__':
    pass