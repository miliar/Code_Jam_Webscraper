import sys

def main():
    inFile=open("E:\\Python\\D-small-attempt4.in","r")
    sys.stdin=inFile
    outFile=open("E:\\Python\\D-small-attempt4.out","w")
    sys.stdout=outFile    
    TC=int(input())
    for c in range(1,TC+1):
        s=input()
        s=[int(x) for x in s.split()]
        X=s[0]
        R=s[1]
        C=s[2]
        if X==1:
            winner='GABRIEL'
        elif X==2:
            if (R*C)%2==0:
                winner='GABRIEL'
            else:
                winner='RICHARD'
        elif X==3:
            if ((R*C)%3==0) and (R>1) and (C>1):
                winner='GABRIEL'
            else:
                winner='RICHARD'
        elif X==4:
            if (R==3 and C==4) or (R==4 and C==3) or (R==4 and C==4):
                winner='GABRIEL'
            else:
                winner='RICHARD'
        print("Case #{}: {}".format(c,winner))
    outFile.close()

main()
        
