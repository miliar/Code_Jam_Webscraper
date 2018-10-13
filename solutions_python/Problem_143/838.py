location = 'D:\\Saved Stuff\\'
import itertools

inp=[]
results=[]

with open(location+'lotto.in','r') as f:
    count = 0
    for each in f:
        if count!=0:
            inp.append(each[:-1])
        else:
            cases=int(each)
        count+=1

inpp=[]

x = list(itertools.product(*[('0', '1')] * 20))



def binary(number):
    n = 0
    count=0
    for each in str(number):
        if each=='1':
            n=n+(2**count)
        count+=1
    return n

binarylist={binary(''.join(b)):''.join(b) for b in x}

def listgen(number):
    count=0
    output=[]
    while count<number:
        output.append(binarylist[count])
        count+=1
    return output

def multiplier(n1,n2):
    out=''
    for each in range(len(n1)):
        if n1[each]=='1' and n2[each]=='1':
            out+='1'
        else:
            out+='0'
    return out

for each in inp:
    inpp.append(each.split())

c=1
for each in inpp:
    oldnum=listgen(int(each[0]))
    newnum=listgen(int(each[1]))
    catnum=listgen(int(each[2]))
    count=0
    for i in oldnum:
        for e in newnum:
            if multiplier(i,e) in catnum:
                count+=1
    results.append('Case #'+str(c)+': '+str(count))
    c+=1
    

with open(location+'lotto.out','w') as f:
    for each in results:
        print each
        f.write(each+'\n')
   




    
