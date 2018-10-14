#
import re
import math
         
f = open("A-large.in","r")
fo = open("A_large.out","w")



lines = f.readlines()
lines = [l.strip() for l in lines]
i = 0
T = int(lines.pop(0))
for icase in range(T):
      # set parameters
      line = lines.pop(0)
      a = line.split(" ")
      #leng = int(a[0])
      ans = 0
      ad0 = int(a[1][0])
      #print(a)
      for j,n in enumerate(a[1][1:]):
            jj = int(j) + 1
            nn = int(n)
            app =  max(0, jj - ad0 )
            ans += app
            ad0 += nn + app 
            #print(jj,nn,ans,ad0)
      #print(ans)
      print("Case #",icase+1,": ",ans,sep="",file=fo)
      print("Case #",icase+1,": ",ans,sep="")
          
#print("Case #",icase+1,": ",nswitch,sep="",file=fo)
f.close()
fo.close()

