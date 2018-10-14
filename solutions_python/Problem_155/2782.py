
def func(num,strs):
    pre=int(strs[0])
    res=0
    for i in range(1,len(strs)):#str[1:]:
        tmp=int(strs[i])
        if pre<i:
            need=i-pre
            res+=need
            pre+=tmp+need
        else:
            pre+=tmp
    return res
            
f = open("A-large.in")
line = f.readline()
num=int(line)
lists1=[i for i in range(num)]
lists2=[i for i in range(num)]
for i in range(num):            
    line = f.readline()
    line=line.strip('\n')
    line=line.split(' ')
  
    lists1[i]=int(line[0])
    lists2[i]=line[-1]
f.close()
for i in range(num):
    print ('Case #%d: %d'%(i+1, func(lists1[i],lists2[i])))
    