file = open("B-large.in")
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
    days=0.0
    init=2.0
    inp=l[ptr].split()
    ptr+=1
    c=float(inp[0])
    f=float(inp[1])
    x=float(inp[2])
    while True:
        if x/init > ((c/init) +(x/(init+f))):
                days+=c/init
                init=init+f
        else:
                days+=x/init
                break
    results.append("Case #"+str(i)+": "+str(days))

for e in results:
    print e
        
