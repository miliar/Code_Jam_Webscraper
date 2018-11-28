import math

fp = open("C-small-attempt0.in")
fx = open("out.txt",'w+')
t = int(fp.readline())

def pali(word):
    return word == word[::-1]

def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False

def fs(word):
    if pali(word):
        n = int(word)
        if is_square(int(n)):
            if pali(str(int(math.sqrt(n)))):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
            
for case in range(t):
    intv = fp.readline().strip()
    
    a,b = int(intv.split(" ")[0]),int(intv.split(" ")[1])
    cnt=0
    for i in range(a,b+1):
        if fs(str(i)):
            print(i)
            cnt+=1
            
    print("Case #"+str(case+1)+": "+str(cnt),file=fx) 
       
fp.close()
fx.close()
