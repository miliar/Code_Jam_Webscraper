from decimal import Decimal
import sys
import math

inp = open('C:\\Users\\administrator\\Desktop\\GCJ14\\inp.txt', 'r')
out = open('C:\\Users\\administrator\\Desktop\\GCJ14\\out.txt', 'w')
list1=[]
list2=[]
check =0
def test(list1,list2,case):
    res= set(list1)&set(list2)
    if(len(res)==0):
        outputter="Volunteer cheated!"
    elif(len(res)>1):
        outputter="Bad magician!"
    else:
        outputter = "".join(str(e) for e in res)
    output = "Case #"+str(case)+": "+outputter
    print (output)
    out.writelines("%s\n" % output)

def formatinput(list1,count):
    count=count*10
    counter = 1
    xcount=1
    case = 1
    while(xcount<=count):
        x1=list1[xcount-1]
        x2=list1[xcount+4]
        listfirst = list1[xcount+x1[0]-1]
        listsecond = list1[xcount+x2[0]+4]
        test(listfirst,listsecond,case)
        case = case + 1
        xcount=xcount+10
    
for line in inp.readlines():
    if check==0:
        count = int(line)
        check = 1
    else:
        case = 1
        list1.append(map(int,list(line.split())))        
formatinput(list1,count)

out.flush()
out.close()
inp.close()
        
                
    
