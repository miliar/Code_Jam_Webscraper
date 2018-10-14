def inil(aL, r1, c1):
    a = 0
    aLL =[]
    while a <r1:
        aLL.append([])
        b=0
        while b < c1:
            aLL[a].append('.')
            b +=1
        a +=1
    return aLL
            
bL=[]
def repc(aL):
    ret = True
    r = len(aL)
    c = len(aL[0])
    global bL
    bL= inil(aL, r, c)
    n =0
    while n <r:
        m=0
        while m < c:
            if aL[n][m] =='#' and bL[n][m]=='.':
                if n==r-1 or m==c-1:
                    ret = False
                    return ret                    
                elif aL[n][m+1]=='#' and aL[n+1][m] =='#' and aL[n+1][m+1] =='#':
                    bL[n][m]='/'
                    bL[n][m+1]='\\'
                    bL[n+1][m]='\\'
                    bL[n+1][m+1]='/'
                else:
                    ret = False
                    return ret
            m+=1
        n+=1
    return ret


def toInt(aList):
    temp = []
    for key in aList:
        temp.append(int(key))
    return temp

input1 = open(r"c:\googlecode\A-large.in")
lines = input1.readline()
totalC= int(lines.strip('\n'))
case =1
output1 = open(r"c:\googlecode\3Abig.txt", 'w')
lines = input1.readline()
while lines !='':    
    lines = lines.strip("\n")
    tempL = lines.split(' ')
    tempL = toInt(tempL)
    R = tempL[0]
    C = tempL[1]
    n =1
    D=[]
    while n <= R:
        lines = input1.readline().strip("\n")
        D.append(lines)
        n +=1
    x = repc(D)
    out= "Case #"+ str(case) +":\n"
    if x ==True:
        for k in bL:
            for k1 in k:
                out +=k1
            out +='\n'
    else:
        out +='Impossible\n'
    output1.write(out)
    case +=1
    print D
    lines = input1.readline()

output1.close()
input1.close()


    

    
