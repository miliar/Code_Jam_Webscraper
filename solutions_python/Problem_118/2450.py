infile=open('C-small-attempt0.in','r')
try :
   outfile=open('output.txt','w')
except :
   outfile=open('output.txt','x')

import math

def reverse(n):
   st=str(n)
   for i in range(0,len(st)//2):
      if st[i]!=st[len(st)-1-i]:
         return False
   return True

st=infile.readline()
n=int(st)
for i in range(1,n+1):
   st=infile.readline()
   st=st.replace('\n','')
   sp=st.split(' ')
   begin=int(sp[0])
   end=int(sp[1])
   s=0
   for x in range(begin,end+1):
      sq=math.sqrt(x) % 1
      if sq==0.0 and reverse(x) and reverse(int(math.sqrt(x))):
         s+=1
   st='Case #'+str(i)+': '
   outfile.write(st)
   outfile.write(str(s))
   outfile.write('\n')

infile.close()
outfile.close()
