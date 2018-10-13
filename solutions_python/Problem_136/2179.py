def jamImport(str): 
    f= open(str,'r')
    data = f.read()
    f.close()
    return data.split('\n')

def str2list(str):
    return map(float, str.split())

def func(n,c,f,x):
    if n==1 : 
        return x/2.0; 
    elif n == 2:
        return (c/2.0 + x/(2.0+f))
    elif n > 2: 
        return sum([c/(2+ele*f) for ele in range(0,n-1)])+x/(2+f*(n-1))

def delta_func(n,c,f,x):
    return x/(2.0+n*f) + c/(2+(n-1)*f) -x/(2+(n-1)*f)

# start code

data = jamImport('B-large.in.txt')
numCases = int(data[0])

# store result
resFile = open('solutionA.txt','w')

for ele in range(1,numCases + 1):
    c, f, x = str2list(data[ele])
    n = 1;  
    while delta_func(n,c,f,x) < 0:
        n = n + 1
    res = func(n,c,f,x)
    resFile.write('Case #'+str(ele)+': '+('%.7f'% res) + '\n')

resFile.close()

