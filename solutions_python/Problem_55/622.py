f_name = 'small'

fin = open(f_name + '.in',"r")
fout = open(f_name + '.out',"w")

c = 0
x = int(fin.readline())
r=0;k=0;data=[];cost=0;i=0;item=0;n=0
while x>0:
    r,k,n = [int(i) for i in fin.readline().split()]
    data = [int(i) for i in fin.readline().split()]
    
    cost=0
    for i in xrange(0,r):
        s=0;i=0
        while True:
            item = data.pop(0)
            s += item
            i+=1
            data.append(item)            
            if i==len(data) or (s + data[0]) >k :break
        cost+=s
    fout.write("Case #"+str(c+1) +": "+str(cost) +"\n")
            
    c+=1
    x-=1


fin.close()
fout.close()
