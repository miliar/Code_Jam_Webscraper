
def checkCase(data):
    elements=[]
    nonbase=[]
    opposed=[]
    for i in xrange(0, int(data[0])):
        nonbase.append((data[i+1][0],data[i+1][1],data[i+1][2]))
    data=data[int(data[0])+1:]
    for i in xrange(0, int(data[0])):
        opposed.append((data[i+1][0],data[i+1][1]))
    data=data[-1]
    for cmd in data:
        try:
            if len(elements) > 0:
                for n in nonbase:
                    if (n[0] == elements[-1] and cmd == n[1]) or (n[1] == elements[-1] and cmd == n[0]):
                        elements[-1]=n[2]
                        1/0
            for o in opposed:
                if (o[0] in elements and cmd == o[1]) or (o[1] in elements and cmd == o[0]):
                    elements=[]
                    1/0
            elements.append(cmd)
        except:
            pass
    return str(elements).replace("'","")


data=open("B-large.in","r").read()


data=data.splitlines()[1:]
out=open("out.txt","w")

for c in xrange(0, len(data)):
    tmp=data[c].split(" ")
    out.write("Case #%i: %s\n"%(c+1,checkCase(tmp)))
    
out.close()