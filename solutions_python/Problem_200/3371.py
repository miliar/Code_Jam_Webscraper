t=int(input())
i=1
a=[]
while t>0:
		n=int(input())
		a.append(n)
		t-=1
for j in range(len(a)):
  if(a[j] < 10):
    f="Case #"+str(j+1)+": "+str(a[j])
    print(f)
  else: 
    last=list(str(a[j]))
    i=0
    while i<len(last)-1:
      if int(last[i])>int(last[i+1]):
        last[i]=str(int(last[i])-1)
        for k in range(i+1,len(last)):
          last[k]='9'
        i=0
      else:
        i+=1
    f="Case #"+str(j+1)+": "+str(int(''.join(last)))
    print(f)