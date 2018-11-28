t=int(input())
i=1
arr=[]
while t>0:
		n=int(input())
		arr.append(n)
		t-=1
for z in range(len(arr)):
  if(arr[z] < 10):
    pp="Case #"+str(z+1)+": "+str(arr[z])
    print(pp)
  else: 
    lastno=list(str(arr[z]))
    i=0
    while i<len(lastno)-1:
      if int(lastno[i])>int(lastno[i+1]):
        lastno[i]=str(int(lastno[i])-1)
        for j in range(i+1,len(lastno)):
          lastno[j]='9'
        i=0
      else:
        i+=1
    pp="Case #"+str(z+1)+": "+str(int(''.join(lastno)))
    print(pp)