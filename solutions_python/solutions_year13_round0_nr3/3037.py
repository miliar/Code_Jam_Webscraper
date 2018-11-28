def IsPalin(number):
    return str(number)==str(number)[::-1]

def GiveRange(a,b):
    return(math.ceil(a**.5),math.floor(b**.5))

def ReturnPalinList(a,b):
    l=[]
    for i in range(a,b):
        if IsPalin(i):
            l.append(i)
    return l

def FandS(num1,num2):
    res = 0
    (a,b)=GiveRange(num1,num2)
    for i in range(a,b+1):
        if IsPalin(i):
            if IsPalin(i**2):
                res+=1
    return(res)

def FileFandS(Filename,Output):
    with open(Output,mode='w',encoding='utf-8') as wr_file:
        with open(Filename,encoding='utf-8') as a_file:
            NumLines = int(a_file.readline())
            for i in range(NumLines):
                (sNum1,sNum2)=a_file.readline().split()
                res=FandS(int(sNum1),int(sNum2))
                print ('Case #{0}: {1}'.format(i+1,res),file=wr_file)

def testFandS(num1,num2):
    res = []
    (a,b)=GiveRange(num1,num2)
    for i in range(a,b+1):
        if IsPalin(i):
            if IsPalin(i**2):
                res.append(i)
    return(res)

if __name__ == '__main__':
    FileFandS('C-small-attempt0.in','C-small-attempt0-solution.txt')
