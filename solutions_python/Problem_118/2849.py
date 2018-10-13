import math
#read the lines
nlines=[]
for line in open('C-small-attempt0.in','r'):
    nlines.append(line)

lines=[]


#removing the \ns
for line in nlines:    
    if line.endswith('\n'):
        line=line[:-1]
    lines.append(line)

#taking no of cases
t=int(lines[0])

lines=lines[1:]
##print(lines)
##print(t)
cno=0

#getting results
for line in lines:
    cno+=1
    limits=list(line.split(' '))
##    print(limits)
    count=0
    l=int(limits[0])
    h=int(limits[1])+1
    for i in range(l,h):
##        print('i='+str(i))
        sq=round(math.sqrt(i))
##        print('sq='+str(sq))
        if(int(str(sq)[::-1])==sq):
                if(int(str(i)[::-1])==i):
                       if(sq*sq==i):
                           count+=1
    print('Case #'+str(cno)+': '+str(count))
