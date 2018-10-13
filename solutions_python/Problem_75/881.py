import sys

cases=int(sys.stdin.readline())

def check_opposed(list, opposed):
   for (a,b) in opposed:
      if a in list and b in list:
         return []
   return list

def check_combine(list, combine):
   if len(list)<2:
      return list
#   print list
   for (a,b,c) in combine:
      if(list[-1]==a and list[-2]==b) or (list[-1]==b and list[-2]==a):
         list.pop()
         list.pop()
         list.append(c)
         return check_combine(list, combine)
   return list

for j in range(0, cases):
   opposed=[]
   combine=[]
   line=sys.stdin.readline().split()   
#   print line
   i=0
   for k in range(0, int(line[i])):
      i+=1
      combine.append((line[i][0], line[i][1], line[i][2]))
   i+=1
   for k in range(0, int(line[i])):
      i+=1
      opposed.append((line[i][0], line[i][1]))
   i+=1
   stack=[]
   for k in range(0, int(line[i])):
#      print line[i], k
      stack.append(line[i+1][k])
      stack=check_combine(stack, combine)
      stack=check_opposed(stack, opposed)
   out=str(stack)
   out=out.replace("'", "")
   print "Case #%d: %s"%(j+1, out)
