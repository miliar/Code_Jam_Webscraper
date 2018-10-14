f=open('B-large.in',"r")
w=open('output2-large.txt',"w")

cases=int(f.readline())

def timeCompare(income,C,F,X):
    notBuy=X/income
    buy=C/income+X/(income+F)
    if notBuy<buy:
        return False
    else:
        return True

def getCookies(C,F,X):
    income=2.0
    total=0.0
    while(timeCompare(income,C,F,X)):
        total=total+C/income
        income=income+F
    total=total+X/income
    return total

def readfile(f):
    line=f.readline()
    temp=line.split(' ')
    C=float(temp[0])
    F=float(temp[1])
    X=float(temp[2])
    return C,F,X
for i in range(cases):
    C,F,X=readfile(f)
    time=getCookies(C,F,X)
    result="Case #%d: %.7f"  % (i+1,time)
    result=result+"\n"
    w.write(result)
w.close()

