input = open("input.txt","r")    
output = open("output.txt","w+")
cases = int(input.readline())

for case in range(1,cases+1):
    print("--")
    n = int(input.readline())
    if(n>1):
        wir = 0
        a1,a2 = map(int,input.readline().split())
        b1,b2 = map(int,input.readline().split())
        if(a1>b1 and a2>b2):
            output.write("Case #%d: 0\n"%case) 
            wir = 1
        if(a1<b1 and a2<b2):
            output.write("Case #%d: 0\n"%case)
            wir = 1
        if(wir == 0): output.write("Case #%d: 1\n"%case)    
    else:
        input.readline()
        output.write("Case #%d: 0\n"%case)    