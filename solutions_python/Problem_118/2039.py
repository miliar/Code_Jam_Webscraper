import math


list1 = []
lowest = int(math.ceil(math.sqrt(1)))
heighest = int(math.sqrt(10**14))
for n in range(lowest, heighest + 1):
    y = n ** 2
    if str(y) == str(y)[::-1]:
        y1 = int(math.sqrt(y))
        if str(y1) == str(y1)[::-1]:
            list1.append(y)

def pal(a,b):
    count = 0
    a,b = int(a),int(b)
    for i in list1:
        if i >=a and i <=b:
            count += 1
    return count

fin = open('large.in')
b = open('result.in','w')      

n=1
case=1
                
for i in fin:
    if n >=2:
        list = i.split()
        a1,b1 = list[0],list[1]
        line = 'Case #%d: %d\n'%(case,pal(a1,b1))
        case += 1
        b.write(line)
    n += 1



