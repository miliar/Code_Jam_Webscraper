#python version 2.7 - R1C - Problem B
import math
def solveProblem(fileName):
    
    fileIn=file(fileName)
    fileOut=file(fileName[:-2]+'out', 'w')
    
    T=int(fileIn.readline())
    
    for caseNum in xrange(1,T+1):
        print caseNum
        data=fileIn.readline()
        D, N, A=[float(i) for i in data.strip('\n').split(' ')]
        N = int(N)
        OC =[]
        for n in xrange(N):
            OC.append([float(i) for i in fileIn.readline().strip('\n').split(' ')])
        A_list = [float(i) for i in fileIn.readline().strip('\n').split(' ')]
        answers=[solveCase(D,OC,a) for a in A_list]
        fileOut.writelines("Case #%d:\n" % (caseNum,))
        for answer in answers:
            print answer
            fileOut.writelines("%s\n" % (answer,))
        
    print 'Done'
    fileIn.close()
    fileOut.close()

def solveCase(D,OC,a):
    #caculate Td, D
    OC1=[v for v in OC if v[1]<=D]
    if len(OC1)==0:
        OC=[[0.0,D]]
    else:
        if OC1[-1][1]==D:
            OC=OC1
        else:
            OC2=[v for v in OC if v[1]>D]
            s=(OC2[0][1]-OC1[-1][1])/(OC2[0][0]-OC1[-1][0])
            td=(D-OC1[-1][1])/s+OC1[-1][0]
            OC1.append([td,D])
            OC=OC1
    
    ###
    MC=[[0.0,0.0]]
    N=len(OC)
    for i in xrange(N):
        Vms=MC[-1][1]
        Tms=MC[-1][0]
        if i == 0:
            Xm=0
        else:
            Xm=OC[i-1][1]
        Ti=OC[i][0]
        Xi=OC[i][1]
        T=Ti-Tms
        X=Xi-Xm
        Vme=0
        Tme=0
        #Caculate Vme Tme
        #if m can catch o
        if (Vms*T + 0.5*a*T*T)>X:
            Tme=Ti
            Vms1=(X-0.5*a*T*T)/T
            if Vms1<0:
                Vms1=0
                Ttemp=math.sqrt(X/(0.5*a))
                Vme=a*Ttemp
                
            else:
                Vme=Vms1+a*T
                
            
        #m can't catch o
        else:
            a1=0.5*a
            b=Vms
            c=-1*X
            Tme=Tms+getT(a1,b,c)
            Vme=Vms+a*(Tme-Tms)
        MC.append([Tme,Vme])

    
    return '%.7f'%MC[-1][0]


def getT(a,b,c):
    m=b**2-4*a*c
    if m<0:
        print 'error'    
        return -1
    else:
        k=m**(0.5)
        t1=(-b+k)/(2*a)
        t2=(-b-k)/(2*a)
        if t1>=0:
            return t1
        elif t2>=0:
            return t2
        else:
            print 'error'
            return -1
                
                
if __name__ == '__main__':
    fileName= r'C:\Users\i035514\Desktop\Codejam\R1C\B-small-attempt1.in'
    solveProblem(fileName)