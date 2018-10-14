
def checkCase(data):
    rest=0
    for i in xrange(0, len(data)):
        if data[i]!=i+1:
            rest+=1
    return rest


data=open("D-large.in","r").read()

data=data.splitlines()[1:]
out=open("out.txt","w")

for c in xrange(1, len(data),2):
    tmp=[int(i) for i in data[c].split(" ")]
        
    out.write("Case #%i: %i\n"%(c/2+1,checkCase(tmp)))
    
out.close()