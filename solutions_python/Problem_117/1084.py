
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
      horizontal=[]
      for y in range(0,M):
    
       horizontal.append(patt[x][y])
      horizontal.sort()
      max_h=horizontal[M-1]
      for y in range(0,M):
       if new[x][y]>max_h:
        new[x][y]=max_h
     
     for j in range(0,M):
      vertical=[]
      for i in range(0,N):
       vertical.append(patt[i][j])
      vertical.sort()
      max_v=vertical[N-1]
      for i in range(0,N):
       if new[i][j]>max_v:
        new[i][j]=max_v
    ct=0
    for x in range(0,N):
     for y in range(0,M):
      if patt[x][y]==new[x][y]:
       ct+=1
    ck=N*M
    if ct==ck:
       return "YES"
    else:
       return "NO"
    
 
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
    
    

