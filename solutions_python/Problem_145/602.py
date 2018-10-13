import math
file = open("A-small-attempt0.in")
l=[]
while 1:
	line=file.readline() 
	if not line:
		break
	l.append(line)

ptr=0
t=int(l[ptr])
ptr+=1
i=0
results=[]

while i<t:
    i+=1
    ancestor=l[ptr]
    ptr+=1
    ancList=ancestor.split('/')
    num=int(ancList[0],10)
    den=int(ancList[1],10)
    height=math.log(den,2)
    if height ==int(height):
        j=0
        while True:
            val=math.pow(2,j)
            if num/(den*1.0)>=1/(val*1.0):
                break                
            j+=1
        results.append("Case #"+str(i)+": "+str(j))
    else:
        results.append("Case #"+str(i)+": impossible")
    
for e in results:
    print e
        
