def marcaFin(n):
    ainit=0
    init=0
    final=0
    for x in range(len(n)):
        if n[x]=='1':
            if x-ainit>final-init:
                init=ainit
                final=x
            ainit=x
    y=final-init-2
    return y

def marca(n):
    ainit=0
    init=0
    final=0
    for x in range(len(n)):
        if n[x]=='1':
            if x-ainit>final-init:
                init=ainit
                final=x
            ainit=x
    y=(final+init)//2
    n[y]='1'
    return n

def marcaTodos(v, n):
    for x in range(n-1):
        v=marca(v)
    return v

def separa(s):
    cont=0
    r1=""
    r2=""
    flag=True
    while flag:
        if s[cont]!=' ':
            r1+=s[cont]
        else:
            flag=False
        cont+=1
    while cont<len(s):
        if s[cont]!=' ':
            r2+=s[cont]
        cont+=1
    return [int(r1),int(r2)]

def createBath(d):
    res=['1']
    for x in range(d):
        res.append('0')
    res.append('1')
    return res

i = int(input())
numbers = []
for a in range(i):
    s = input()
    numbers.append(separa(s))

res = "Case #%d: %s"

for a in range(i):
    b = createBath(numbers[a][0])
    v = marcaTodos(b, numbers[a][1])
    aux = marcaFin(v)
    maior=0
    menor=0
    if aux%2==0:
        maior=aux//2
        menor=aux//2
    else:
        menor=aux//2
        maior=menor+1
    print(res%(a+1, str(maior)+" "+str(menor)))