f = open('fin1.in', 'r+')
open('fout1.txt', 'w').close()
n = open('fout1.txt', 'r+')
l =  int(f.readline())
cases=[]
for line in f:
    cases.append(int(line))
def check(num):
    num = list(str(num))
    for j in range(len(num)-1):
        if(int(num[j])>int(num[j+1])):
            return False
    return True
def last(num):
     num = list(str(num))
     for j in range(len(num)-1):
        if(int(num[j])>int(num[j+1])):
            return j+1
     return 0
  
def tidy(num):
    print(num)
    if check(num):
        return num
    num = list(str(num))
    l = last("".join(num))
    if int(int(num[l])==0):
        num[l-1]=str(int(num[l-1])-1)
        num[l]=str(9)
        for g in range(len(num)-l):
            num[l+g]=str(9)
    else:
        num[l]=str(int(num[l])-1)
    
    print(num)
    return tidy("".join(num).lstrip("0"))
        
for c in range(len(cases)):
    n.write("Case #" +str(c+1)+": "+str(tidy(cases[c]))+"\n")

n.close()
f.close()
