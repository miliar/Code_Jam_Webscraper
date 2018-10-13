__author__ = 'majid'
def f(a,an,b,bn):
    ase=set(a[an-1])
    bse=set(b[bn-1])
    if len(ase.intersection(bse))==0:
        return "Volunteer cheated!"
    elif len(ase.intersection(bse))>=2:
        return "Bad magician!"
    else:
        return str(ase.intersection(bse).pop())
x=open("A-small-attempt2.in")
fo=open("A-small-attempt2.out","w")
n=int(x.readline())
for i in range(n):
    an=int(x.readline())
    a=[]
    a.append([int(ir) for ir in x.readline().split()])
    a.append([int(ir) for ir in x.readline().split()])
    a.append([int(ir) for ir in x.readline().split()])
    a.append([int(ir) for ir in x.readline().split()])
    bn=int(x.readline())
    b=[]
    b.append([int(ir) for ir in x.readline().split()])
    b.append([int(ir) for ir in x.readline().split()])
    b.append([int(ir) for ir in x.readline().split()])
    b.append([int(ir) for ir in x.readline().split()])
    print("Case #"+str(i+1)+": "+f(a,an,b,bn))
    fo.write("Case #"+str(i+1)+": "+f(a,an,b,bn)+"\n")
fo.close()
x.close()
