from math import sqrt, ceil

def pal(num):
    s=str(num)
    return(all(a==b for a,b in zip(s[:len(s)], reversed(s))))

def fair(a, b):
    a=int(ceil(sqrt(a)))
    b=int(sqrt(b))
    c=[]
    for i in range(a,b+1):
        if pal(i):
            q=pow(i,2)
            if pal(q):
                c.append(q)
    return c

init=(1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004)

def between(a,b):
    c=0
    for num in init:
        if a<=num<=b:
            c+=1
    return c

file=open(r"C:\Users\user\Downloads\C-large-1.in").read().split('\n',1)[1]

for i, line in enumerate(file.splitlines()):
    print("Case #"+str(i+1)+":", between(*map(int, line.split(' '))))
