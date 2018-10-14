#!usr/bin/python
import math

f=open("/home/soumeng/Documents/gcjam/C-small-attempt0.in","r")
w=open("/home/soumeng/Documents/gcjam/fair_square.out", "w+a")
r=f.read()
cont=r.split('\n')
test=int(cont.pop(0))
cont.pop()
final_str='Case#'

for i in range(test):
    each=str(cont[i])
    st=each.split()
    lw=int(st[0])
    up=int(st[1])
    
    count=0
    for j in range(lw, up+1):
        num=math.sqrt(j)
        str1='Case #'
        str2=':'
        str1=str1+str(i+1)+str2
        if num/int(num)==1:
            st=str(int(num))
            st1=str(j)
            if st==st[::-1] and st1==st1[::-1]:
                count=count+1
                
            else:
                pass
                    
        else:
            pass
    str3=str1+" "+str(count)
    w.write(str3)
    w.write("\n")
f.close()
w.close()
        
    
