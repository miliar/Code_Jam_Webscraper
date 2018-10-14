import decimal
def f(C,F,X):
    rt = 2
    tm = 0
    while  X/(rt+F)<= (X-C)/rt:
        tm+=C/rt
        rt+=F
    tm+= X/rt
    w = decimal.Decimal(tm)
    return(round(w,7))

fh = open("B-large.in",'r')
gh = open("B-large-Output.txt",'w')

t = int(fh.readline().strip())
for i in range(t):
    gh.write("Case #"+str(i+1)+": ")
    l = fh.readline().strip().split()
    gh.write(str(f(eval(l[0]),eval(l[1]),eval(l[2])))+"\n")
fh.close()
gh.close()

    
