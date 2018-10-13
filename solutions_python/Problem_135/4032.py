lin=int(raw_input())
ret=""
for i in range(lin):
   f=int(raw_input())-1
   row=[]
   for x in range(4):
       row.append(raw_input())
   fila=row[f]
   nums1=fila.split(" ")
   f=int(raw_input())-1
   row=[]
   for x in range(4):
       row.append(raw_input())
   fila=row[f]
   nums2=fila.split(" ")
   si=False
   save=[]
   for n in nums1:
       if n in nums2:
           save.append(n)
   if len(save)==1:
       ret+="Case #"+str(i+1)+": "+str(save[0])+"\n"
   elif len(save)>1:
       ret+="Case #"+str(i+1)+": Bad magician!\n"
   else:
       ret+="Case #"+str(i+1)+": Volunteer cheated!\n"
print ret