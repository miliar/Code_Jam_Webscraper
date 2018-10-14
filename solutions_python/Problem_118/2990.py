def palin(x):
    s=''
    for i in range(len(x)):
        s=x[i]+s
    if s==x:
        return True
    else:
        return False


def square(x):
    z=int(x**0.5)
    if x==z*z:
        return True
    else:
        return False
    

def fas(x):
    if not palin(x):
        return False
    if not square(int(x)):
        return False
    if palin(str(int(int(x)**0.5))):
        return True
    return False


testcases = int(input())
for t in range(1, testcases + 1):
    n=raw_input()
    n1=n.split(' ')
    n2=int(n1[0])
    n3=int(n1[1])
    c=0
    for i in range(n2,n3+1,1):
        if fas(str(i)):
            c+=1
    print 'Case #' + str(t) + ': '+str(c)
    

    
