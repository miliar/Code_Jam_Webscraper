#!/usr/bin/python
##reading input file.....
fname=raw_input("input filename:")
data=open(fname,"r+")
text=data.readlines()
data.close()
nos=int(text[0])
nos=nos
tn=1

def main(N,M,patt):
    if N==1 or M==1:
     return "YES"
    else:
     new=[[100 for x in range(0,M)] for y in range(0,N)]
     for x in range(0,N):
      hr=[]
      for y in range(0,M):
    
       hr.append(patt[x][y])
      hr.sort()
      mah=hr[M-1]
      for y in range(0,M):
       if new[x][y]>mah:
        new[x][y]=mah
     
     for j in range(0,M):
      vr=[]
      for i in range(0,N):
       vr.append(patt[i][j])
      vr.sort()
      mav=vr[N-1]
      for i in range(0,N):
       if new[i][j]>mav:
        new[i][j]=mav
    count=0
    for x in range(0,N):
     for y in range(0,M):
      if patt[x][y]==new[x][y]:
       count+=1
    check=N*M
    if count==check:
       return "YES"
    else:
       return "NO"
    
        
##   For printing output...   
def fun(N,M,tn,x):
    pat=[]
    for i in range(0,N):
     ln=text[tn+1+i]
     ln=ln.strip()
     ll=ln.split()
     pat.append(ll)
    patt=[[int(i) for i in y] for y in pat]
    value=main(N,M,patt)
    out=open("out.txt","a+")
    out.writelines("Case #%d: %s \n" %(x,value))     
    out.close()
   
for x in range(0,nos):
    line=text[tn]
    line=line.strip()
    lin=line.split()
    N=int(lin[0])
    M=int(lin[1])
    fun(N,M,tn,x+1)
    tn=tn+N+1
    
    

print "Result is stored in out.txt file successfully!!"
