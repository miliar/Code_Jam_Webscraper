import math 

def wf(fileName,ls):
    f = open(fileName,'w')
    for i,l in enumerate(ls):
        f.write('Case #%d: %.6f\n'%(i+1,l))

def minR(ls):
    max1 = 0
    max2 = 0
    maxDis = ls[0][2]
    
    for i in range(len(ls)-1):
        for j in range(i+1,len(ls)):
            dis = math.sqrt((ls[i][0]-ls[j][0])*(ls[i][0]-ls[j][0])+(ls[i][1]-ls[j][1])*(ls[i][1]-ls[j][1]))+ls[i][2]+ls[j][2]
            print dis
            if dis>maxDis:
                maxDis = dis
                max1 = i
                max2 = j
    print max1,max2,maxDis
        
    maxDis1 = 0
    maxDis2 = 0
    for l in ls:
        dis1 = math.sqrt((l[0]-ls[max1][0])*(l[0]-ls[max1][0])+(l[1]-ls[max1][1])*(l[1]-ls[max1][1]))+l[2]+ls[max1][2]
        dis2 = math.sqrt((l[0]-ls[max2][0])*(l[0]-ls[max2][0])+(l[1]-ls[max2][1])*(l[1]-ls[max2][1]))+l[2]+ls[max2][2]
        print dis1,dis2,maxDis1,maxDis2
        if(dis1<dis2):
            if dis1>maxDis1:
                maxDis1 = dis1
        else:
            if dis2>maxDis2:
                maxDis2 = dis2
    
    print maxDis1,maxDis2
    
    if maxDis1>maxDis2:
        minR = maxDis1/2
    else:
        minR = maxDis2/2
        
    return minR

filename = 'Sample.in'
filename = 'D-small-attempt0.in'
#filename = 'A-large.in'
f = open(filename)
contents = f.readlines()
s =contents[0].strip()
Cases = int(s)
print Cases
lsResult = []
current = 1
for count in range(Cases):
    print count,'\t:',contents[current]    
    n = int(contents[current])    
    current += 1
    
    ls = contents[current:current+n]
    ls = [l.split() for l in ls]
    ls = [[float(l[0]),float(l[1]),float(l[2])] for l in ls]
    print ls
            
    lsResult.append( minR(ls) )
    
    current += n
    
    

#print lsResult

    
wf(filename.split('.')[0]+'.out',lsResult)
