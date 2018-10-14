def check(n):
    a = str(n)
    for i in range(0,len(a)-1):
        if int(a[i+1])<int(a[i]):
            return False
    return True

def rep2dig(x):
    i = x
    fin = 0
    while i>0:
        if check(i):
            fin = i
            break
        else:
            i-=1
    if (fin<10):
        return '0'+str(fin)
    else:
        return str(fin)

def process(x):
    a = str(x)
    b= []
    for i in a:
        b.append(i)
    a = b
    for i in range(0,len(a)-1):
        if a[i+1]<a[i]:
            tem = rep2dig(int(a[i]+a[i+1]))
            a[i] = tem[0]
            a[i+1] = tem[1]
            for j in range(i+1,len(a)):
                a[j] = '9'
    return a

def solve(x):
    a = str(x)
    while True:
        if check(a):
            break
        else:
            k = process(a)
            b = ''
            for i in k:
                b+=i
            a=b
    return int(a)

file = open("B-large.in","r")
cnt = 0
for line in file:
    if cnt==0:
        cnt+=1
    else:
        red = line.strip()
        print("Case #"+str(cnt)+": " + str(solve(red)))
        cnt+=1
