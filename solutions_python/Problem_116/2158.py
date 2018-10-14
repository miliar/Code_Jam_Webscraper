import time
s_time=time.time()


f=open('A-large.in','r')
q= open('result.txt','w')

def check_won(qizi):
    def won(line):
        for e in line:
            if e !='T':
                return e+' won'
    def check_line(data,find_dot):
        for line in data:
            if '.' in line :
                find_dot[0]=True
                continue
            num = len(set(line))
            if num ==1:
                return won(line)
            elif num ==2 and ('T' in line):
                return won(line) 
    def check_conor(data):
        if '.' in data :
            return None
        num = len(set(data))
        if num ==1:
            return won(data)
        elif num ==2 and ('T' in data):
            return won(data) 

    find_dot=[False]
    r=check_line(qizi,find_dot) 
    if r:
        return r

    tmp= zip(qizi[0],qizi[1],qizi[2],qizi[3])
    r=check_line(tmp,find_dot)
    if r:
        return r

    a=[qizi[0][0],qizi[1][1],qizi[2][2],qizi[3][3]]
    b=[qizi[0][3],qizi[1][2],qizi[2][1],qizi[3][0]]
    
    r=check_conor(a)
    if r:
        return r
    
    r=check_conor(b)
    if r:
        return r
    if find_dot[0]:
        return 'Game has not completed'
    else:
        return 'Draw'



f.readline()
count=1
block=0
qizi=[]

for line in f:
    block +=1
    state = block %5
    if state==4:
        qizi.append(list(line[:-1]))
        s='Case #'+str(count)+': '+str(check_won(qizi))+'\n'
        
        qizi=[]
        count +=1  
        q.write(s)
        print 'ok'+str(count-1)
    elif state!=0:
        qizi.append(list(line[:-1]))
 

f.close()
q.close()
print 'seconds:',time.time()-s_time







