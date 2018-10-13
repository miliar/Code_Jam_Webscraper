import sys, math

substr={}

fin=open("a.in","r")
fout=open("a.out","w")
T=fin.readline()
T=int(T)
def check(subl,n):

   global substr
   count=0
   flag=0
   l=len(subl)
   for i in range(l):
        if subl[i]!='a' and subl[i]!='e' and subl[i]!='i' and subl[i]!='o'and subl[i]!='u':
             count=count+1
        else:
             count=0
        if count >= n:
            flag=1
   if flag==1:
     sl=len(substr)
     
     for i,j in substr.items():
          if(j==subl):
             flag=1
   if flag==1:
      sl=len(substr)
      substr[sl]=subl


for i in range(T):
    data=fin.readline()
    L,n=data.split(" ")
    L=str(L)
    n=int(n)
    l=len(L)
    
    for j in range(n,l+1):
         for k in range(l-j+1):
               subl=L[k:k+j]
               check(subl,n)
    
    tot=len(substr)
    substr={}
    case=i+1
    case=str(case) 
    output= "Case #"+case+": "+str(tot)+"\n"
    fout.write(output)    


  

