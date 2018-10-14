
fname=raw_input("input filename:")
data=open(fname,"r+")
text=data.readlines()
data.close()
nos=int(text[0])


def main(r,t):
    check=0
    count=0
    while check<=t:
     z=2*r+1
     r=r+2
     check=check+z
     count+=1
    return count-1
  
def fun(line,x):
    line=line.strip()
    ln=line.split()
    
    r,t=int(ln[0]),int(ln[1])
    value=main(r,t)
    out=open("output.txt","a+")
    out.writelines("Case #%d: %d \n" %(x,value))     
    out.close()
   
for x in range(1,nos+1):
    line=text[x]
    fun(line,x)

