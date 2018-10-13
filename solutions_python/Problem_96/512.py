import sys
sys.stdin=open('B-large.in')
Output=open('Large-outputC-Py.txt','w+')
for test in range(input()):
   temp=raw_input().split()
   N,S,p,t,total=int(temp[0]),int(temp[1]),int(temp[2]),temp[3:],0
   for i in t:
      if (p==0):
         total=N
      elif (p==1):
         if (int(i)!=0):
            total+=1
      elif (int(i)>=p+p+p-2):
          total+=1
      elif (int(i)>=p+p+p-4):
          if (S>0):
             total+=1
             S-=1
   Output.write("Case #%d: %d"%(test+1,total)+"\n")

Output.close()
#print "Done!"
   
