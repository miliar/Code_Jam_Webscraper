def isTidy(x):
    xs = str(x)
    l = len(xs)
    for i in reversed(range(1,l)):
        if(long(xs[i]) >= long(xs[i-1])):
            continue
        else:
            return False
    return True
    
def makeTidy(x):
    xs = str(x)
    l = len(xs)
    for i in reversed(range(1,l)):
        if(long(xs[i]) >= long(xs[i-1])):
            continue
        else:
            sub = (long(xs[i:]))
            sub+=1
            x-=sub
            xs = str(x)
    return x

fin = open("C:\Users\Harsh Shah\Desktop\in.in","r")
fout = open("C:\Users\Harsh Shah\Desktop\out.txt","w")
t = int(fin.readline())

#t = int(input())
for i in range(t):
    n = long(fin.readline())
    #n = int(input())
    print n
    if(isTidy(n)):
        print("Case #{0}: {1}\n".format(i+1,n))
        fout.write("Case #{0}: {1}\n".format(i+1,n))
    else:
        print("Case #{0}: {1}\n".format(i+1,makeTidy(n)))
        fout.write("Case #{0}: {1}\n".format(i+1,makeTidy(n)))
    t-=1
        