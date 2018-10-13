def cross(a,b):
 return (a[0]>b[0] and a[1]<b[1]) or (a[0]<b[0] and a[1]>b[1])

input=file('A-large.in')
output=file('A-large.out','wb+')
for case in range(int(input.readline())):
 data=[]
 for line in range(int(input.readline())):
  data.append([int(x) for x in input.readline().split(' ')])
 m=0
 for x in range(len(data)):
  for y in range(x+1,len(data)):
   if cross(data[x],data[y]): m+=1
 output.write('Case #'+str(case+1)+': '+str(m)+'\n')