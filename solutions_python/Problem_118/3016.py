def palin(s):
   
    if len(s) < 1:
      return True    
    else:
        if s[0] == s[-1]:
          return palin (s[1:-1])
        else:
           return False  

import math
file = open('file.txt', mode='r+')
file2 = open('output.txt',mode='w')
line = file.readline()
list1=[100]
count=0
while True:
    line = file.readline()
    if not line:
     break
    else:
     print line
     
     list1 = line.split(' ')
     print list1
     st=int(list1[0])
     end=int(list1[1])
     counter=0
     for x in range(st,end+1):
         if(palin(str(x))):
            if(math.sqrt(x).is_integer()):
              x1= int(math.sqrt(x))
              if(palin(str(x1))):
                 counter+=1
     count+=1
     file2.write ("Case #%d: %d\n" %(count,counter))
    
