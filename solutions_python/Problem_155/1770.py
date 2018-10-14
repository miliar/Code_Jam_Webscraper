import sys

def main():
    inFile=open("E:\\Python\\A-large.in","r")
    sys.stdin=inFile
    outFile=open("E:\\Python\\A-large.out","w")
    sys.stdout=outFile
    TC=int(input())
    for c in range(1,TC+1):
        s=input()
        s=s.split()
        Smax=int(s[0])
        Slist=[]
        for A in s[1]:
            Slist.append(int(A))
        Fd=0
        Stand=0
        for i in range(Smax+1):
            while Stand<i:
                Fd+=1
                Stand+=1
            Stand+=Slist[i]
        print("Case #{}: {}".format(c,Fd))
        TC-=1
    outFile.close()

main()
        
        
