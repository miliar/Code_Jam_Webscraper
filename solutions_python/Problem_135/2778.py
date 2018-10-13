file = open("A-small-attempt1.in")
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
chosen1=[]
chosen2=[]
results=[]

while i<t:
    i+=1
    j=0
    while j<2:
        j+=1
        row=int(l[ptr])
        ptr+=1
        k=0
        while k<4:
            inp=l[ptr]
            ptr+=1
            if k==row-1 and j==1:
                chosen1=inp.split()

            if k==row-1 and j==2:
                chosen2=inp.split()
            k+=1
    x=0
    while x<4:
        chosen1[x]=int(chosen1[x])
        chosen2[x]=int(chosen2[x])
        x+=1

    count=0
    selected=0
    for e in chosen1:
        if e in chosen2:
            count+=1
            selected=e

    if count>1:
        results.append("Case #"+str(i)+": Bad magician!")
    if count is 0:
        results.append("Case #"+str(i)+": Volunteer cheated!")
    if count is 1:
        results.append("Case #"+str(i)+": "+str(selected))

for e in results:
    print e
        
