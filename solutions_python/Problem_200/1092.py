t=int(input())

for T in range(1,t+1):
    n=int(input())
    for N in range(n,0,-1):
        num=str(N)
        length=len(num)
        success=int(1)
        for i in range(length-1,0,-1):
            if num[i]<num[i-1]:
                success=int(0)
                break
        if success==1:
            print("Case #",T,": ",N,sep="")
            break
