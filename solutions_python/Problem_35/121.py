f = file('B-large.in')
line = f.read()
#print line 
f.close
f=file('B-large.out','w')
list="abcdefghijklmnopqrstuvwxyz"
T = 0
H = 0
W = 0
para=[0,0,0,0]

basin  = []
result = []
output = []
i = 0
color = 0


nu =0
ran =[0,0,0,0,0]
end = 0
tmp1 = 0
tmp2 = 0
#i can be change
number = 0
def change(pa):
   return list[0xffff - pa-1]

while line[i] <= '9' and line[i] >= '0' :    
   number = number * 10 + int (line[i])
   i +=1
i +=1
T = number 
number = 0
for x in range(T):
   while line[i] <= '9' and line[i] >= '0' :    
      number = number * 10 + int (line[i])
      i +=1
   i +=1
   H = number
   number = 0
   while line[i] <= '9' and line[i] >= '0' :    
      number = number * 10 + int (line[i])
      i +=1
   i +=1
   W = number
   number = 0
   para=[0,-W,-1,1,W]
   for y in range(H * W):
      while line[i] <= '9' and line[i] >= '0' :    
         number = number * 10 + int (line[i])      
         i +=1
      i +=1
      basin.append(number)
      number = 0
   nu = 0
   end = H * W
   for y in range(end):
      taken = nu + para[1]
      if taken >= 0:    
         ran[0] = basin[taken]
      else:
         ran[0] = 0xffff
      taken = nu + para[2]
      if taken >= 0 and (taken % W !=W-1):    
         ran[1] = basin[taken]
      else:
         ran[1] = 0xffff  
      taken = nu + para[3]
      if taken < end and (taken % W !=0):    
         ran[2] = basin[taken]
      else:
         ran[2] = 0xffff
      taken = nu + para[4]
      if taken < end:    
         ran[3] = basin[taken]
      else:
         ran[3] = 0xffff 
     # print ran,nu
      tmp1 = 0
      tmp2 = 0
      if basin[nu] <= ran[0]:
         tmp1 = basin[nu]
         tmp2 = 0
      else:
         tmp1 = ran[0]
         tmp2 = 1
      if tmp1 > ran[1]:
         tmp1 = ran[1]
         tmp2 = 2 
      if tmp1 > ran[2]:
         tmp1 = ran[2]
         tmp2 = 3
      if tmp1 > ran[3]:
         tmp2 = 4
      result.append(tmp2)
      nu += 1
   #print result
   tmp1 =0
   tmp2 =0
   tmp3 =[]
   tmp4 =0
   for y in range(end):
      if result[y] < 10000:
         tmp1 = result[y]      
         tmp3.append(y)
         tmp2 = y
         while tmp1 != 0:
            tmp2 += para[tmp1]     
            tmp1 = result[tmp2]
            if result[tmp2] >10000:
               break
            tmp3.append(tmp2)
         if result[tmp2] > 10000:
            tmp4 = result[tmp2]
         else :
            tmp4 = 0xfffe-color
            color+=1
            result[tmp2] = tmp4
         for z in tmp3:
            result[z] = tmp4
         tmp3 =[]
   f.write('Case #%d:\n'% (x+1))
   for  y in range(end):
      f.write('%s'%(change(result[y])))
      if y % W == W-1:
         f.write('\n')
      else:
         f.write(' ')  
   color =0
   output = []   
   basin  = []
   result = []
f.close  
 
