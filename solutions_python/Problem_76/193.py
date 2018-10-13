
def add(a, b):
    return (a|b)-(a&b)

def checkCase(data):
    for k in xrange(1, len(data)):
        data1=data[:k]
        data2=data[k:]
        erg1=0
        for i in data1:
            erg1=add(erg1,i)
        erg2=0
        for i in data2:
            erg2=add(erg2,i)
        if erg1==erg2:
            data.sort()
            data.reverse()
            return sum(data[:len(data2)])
    return "NO"


data=open("C-large.in","r").read()

data=data.splitlines()[1:]
out=open("out.txt","w")

for c in xrange(1, len(data),2):
    tmp=[int(i) for i in data[c].split(" ")]
    out.write("Case #%i: %s\n"%(c/2+1,str(checkCase(tmp))))
    
out.close()