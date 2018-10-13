fin = open('small1.in')
b = open('result.in','w')
import math
def count_pal(a,b):
    a,b = int(a),int(b)
    count = 0
    x = a
    while x>=a and x<=b:
        if str(x) == str(x)[::-1]:
            y = math.sqrt(x)
            if int(y) == y:
                if str(int(y))==str(int(y))[::-1]:
                    
                    count += 1
        x += 1
    return count

n = 1

case = 1

for i in fin:
    if n >=2:
        list = i.split()
        a1,b1 = list[0],list[1]
        line = 'Case #%d: %d\n'%(case,count_pal(a1,b1))
        case += 1
        b.write(line)
    n += 1
