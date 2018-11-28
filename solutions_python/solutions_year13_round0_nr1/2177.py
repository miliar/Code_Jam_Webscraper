def check(st):
 x=0
 o=0
 t=0
 d=0
 for n in st:
  if n=='X':
   x=x+1
  if n=='O':
   o=o+1
  if n=='T':
   t=t+1
  if n=='.':
   d=d+1
 if (x==3 and t==1) or (x==4):
  return "X"
 elif (o==3 and t==1) or (o==4):
  return "O"
 elif d>0:
  return "G"
 else:
  return "U"
fl=open("qrt")
no=int(fl.readline())
for t in range(0,no):
 str1=fl.readline()
 str2=fl.readline()
 str3=fl.readline()
 str4=fl.readline()
 gar=fl.readline()
 r1= check(str1)
 r2= check(str2)
 r3= check(str3)
 r4= check(str4)
 c1=check(str1[0]+str2[0]+str3[0]+str4[0])
 c2=check(str1[1]+str2[1]+str3[1]+str4[1])
 c3=check(str1[2]+str2[2]+str3[2]+str4[2])
 c4=check(str1[3]+str2[3]+str3[3]+str4[3])
 d1=check(str1[0]+str2[1]+str3[2]+str4[3])
 d2=check(str1[3]+str2[2]+str3[1]+str4[0])
 chk=r1+r2+r3+r4+c1+c2+c3+c4+d1+d2
 f1=open("answer","a")
 if(chk.find("X")!=-1):
  f1.write("Case #%s: X won\n"%(t+1))
 elif(chk.find("O")!=-1):
  f1.write("Case #%s: O won\n"%(t+1))
 elif(chk.find("G")!=-1):
  f1.write("Case #%s: Game has not completed\n"%(t+1))
 else:
  f1.write("Case #%s: Draw\n"%(t+1))
