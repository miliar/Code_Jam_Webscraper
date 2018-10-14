#python3

import os
ip=open("C:/Users/Ram/Desktop/CodeJam/B-small-attempt0.in",'r')
op=open("C:/Users/Ram/Desktop/CodeJam/B-small-attempt0.out",'w')
input_array=[]
for line in ip.read().split():
    input_array.append(line)
for x in range(1,int(input_array[0])+1):
    flag=0
    for i in range(int(input_array[x]),0,-1):
        if i>1000 and flag==0:
            var=int('1'+("0"*(len(str(i))-1)))-1
            i=int(var)
            flag=1
        if "".join(sorted(str(i)))==str(i):
            print("Case #"+str(x)+": "+str(i))
            op.write("Case #"+str(x)+": "+str(i)+'\n')
            break
op.close()
ip.close()
