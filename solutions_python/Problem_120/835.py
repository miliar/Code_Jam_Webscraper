import math
f=open('A-small-attempt0.in')
fo=open('A.txt',"w")
lines = []
for line in f.readlines():
        lines.append(line)
f.close()
a = lines.pop(0)
T = int(a)
for case in range(T):
        a = lines.pop(0)
        [R,T] = (a.strip()).split()
        r = int(R)
        t = int(T)
        x = (- 2 * r - 1 + math.sqrt(4*r*r -4*r + 1 + 8*t))/2
        a = int((x+1)/2)
        print('Case #',case+1,': ',a,end='\n',sep='')
        print('Case #',case+1,': ',a,end='\n',sep='',file=fo)
f.close()
fo.close()
        
                
               
