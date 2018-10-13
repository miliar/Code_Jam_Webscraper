t=int(input())
for i in range(0,t):
  len=input().strip().split(" ")
  k=[0]*int(len[1])
  d=[0]*int(len[1])
  time=[0]*int(len[1])
  for j in range(0,int(len[1])):
    inp=input().strip().split(" ")
    k[j]=int(inp[0])
    d[j]=int(inp[1])
    time[j]=(int(len[0])-k[j])/d[j]
  ma=max(time)
  print("Case #"+str(i+1)+": "+'{0:.6f}'.format(int(len[0])/ma))