file = open("input")

counter_i = 1
counter_end_i = file.readline()
num = 1

def judge(string):
    length = len(string)
    dece=0
    k=length
    for x in range(0,length-1):
        if string[x]>string[x+1]:
            k=x
            dece=1
            break
    return dece,k

def solve(string):
    dece,k = judge(string)
    while (dece):
        string = minus_man(string,k)
        #string = str(int(string)-1)
        #print string
        dece,k=judge(string)
    return clean(string)

def clean(string):
    length=len(string)
    list1=list(string)
    for x in range(0,length):
        if list1[x]=="0":
            list1[x]=""
        else:
            break
    string=''.join(list1)
    return string

def minus_man(string,k):
    string = setnew(string,k)
#    length = len(string)
#    list1=list(string)
#    borrow = 1
#    for x in range(0,length):
#        if int(list1[length-1-x])-borrow>=0:
#            list1[length-1-x]=str(int(list1[length-1-x])-borrow)
#            borrow = 0
#        else:
#            list1[length-1-x]="9"
#            borrow = 1
#    string=''.join(list1)
    return string

def setnew(string,k):
    length = len(string)
    list1=list(string)
    for x in range(k+1,length):
        list1[x]="9"
    list1[k]=str(int(list1[k])-1)
    string=''.join(list1)
    return string

    
    

while (counter_i <= int(counter_end_i.strip())):
    num = file.readline().strip()
    counter_i=counter_i+1
    print "%s%d%s%s"%("Case #", counter_i-1, ": ",solve(num))
