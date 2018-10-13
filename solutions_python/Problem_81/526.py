input1 = open(r"c:\googlecode\A-large.in")
#input1 = open(r"c:\googlecode\2Atest.txt")


lines = input1.readline()
totalC= int(lines.strip('\n'))
case =1

def wlm(aList):
    nt = len(aList)
    WL = []
    for k in aList:
        c=0
        wl =[0, 0]
        while c<nt:
            if k[c] =='0':
                wl[1] +=1
            elif k[c] =='1':
                wl[0] +=1            
            c +=1
        WL.append(wl)
    return WL

def ow(wl, aList):
    nt = len(aList)
    n =0    
    WLO={}
    while n <nt:
        WLO[n] = {}
        m=0
        while m < nt:
            if aList[n][m] =='1':
                WLO[n][m]= float(wl[m][0])/(wl[m][0]+wl[m][1]-1)
            elif aList[n][m] =='0':
                WLO[n][m]= float(wl[m][0]-1)/(wl[m][0]+wl[m][1]-1)
            m +=1
        n +=1
    return WLO

def avd(aDic):
    ret = 0.0
    ren = len(aDic)
    for key in aDic:
        ret +=aDic[key]
    ret =ret/ren
    return ret
    

def oow(wl, aDic):
    nt = len(aDic)
    n=0
    oow ={}
    result =0.0
    while n <nt:
        result = 0.25*(float(wl[n][0])/(wl[n][0]+wl[n][1]))
        temp = aDic[n]
        owp =0.0
        owp = avd(temp)
        oowp =0.0
        for key in temp:
            temp1 = aDic[key]
            oowp +=avd(temp1)
        oowp = oowp/len(temp)
        result += 0.50 * owp + 0.25 * oowp
        oow[n] = result
        n +=1
    return oow
    
output1 = open(r"c:\googlecode\2Alarge.txt", 'w')
lines = input1.readline()
while lines !='':    
    lines = lines.strip("\n")
    N = int(lines)
    n =1
    D=[]
    W =[]
    OW={}
    re =0.0    
    while n <= N:
        lines = input1.readline().strip("\n")
        D.append(lines)
        n +=1
    W = wlm(D)
    OW = ow(W, D)
    re = oow(W, OW)
    out= "Case #"+str(case) +":\n"
    for k in re:
        out +=str(re[k]) +"\n"
    output1.write(out)       
    case +=1
    print D
    lines = input1.readline()
output1.close()
input1.close()

