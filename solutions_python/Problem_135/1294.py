import math

def demo():
    a=open("A-small.in")
    b=a.readlines()
    outf=open("out.txt","w")
    
    for i in range(int(b[0])):
        res=check(b[i*10+1+int(b[i*10+1])],b[i*10+6+int(b[i*10+6])])        
        print "Case #"+str(i+1)+": "+str(res)
        outf.write("Case #"+str(i+1)+": "+str(res)+"\n")
    outf.close()

def check(row1,row2):
    r1=row1.split()
    r2=row2.split()
    r=[val for val in r1 if val in r2]
    if len(r)==0:
        ret="Volunteer cheated!"
    elif len(r)==1:
        ret=str(r[0])
    else:
        ret="Bad magician!"
    return ret

raw_input("Got data?")
demo()
