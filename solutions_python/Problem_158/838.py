__author__ = 'Sirna'



gabriel = "GABRIEL"
richard = "RICHARD"

def calc(x,r,c):
    if(x == 1):
        return gabriel
    if(x == 4):
        a = r*c
        if(a==12 or a==16):
            return gabriel
        return richard
    if(x == 2):
        if( (r*c)%2==0):
            return gabriel
        else:
            return richard
    if(x==3):
        if((r*c)%6 ==0 or (r*c)==9):
            return gabriel
        return richard

fname = "a.in"
o = open("d.out","w")
with open(fname) as f:
    content = f.readlines()
    content = [x.strip('\n') for x in content]
    cases = int(content[0])
    for i in range(cases):
        x,r,c = map(int,content[i+1].split())
        print x,r,c,calc(x,r,c)
        o.write("Case #"+str((i+1))+": "+calc(x,r,c)+"\n")
    o.close()