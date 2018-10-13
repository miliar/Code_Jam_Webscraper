def main():
    a=open("B-small-attempt0 (4).in","r")
    b=open("answerrrr.out","w")
    q=int(a.readline())
    u=1
    while(q>0):
        #N=int(a.readline())
        A,B,K=map(int,a.readline().split())
        count=0
        for i in range(A):
            for j in range(B):
                x = i & j
                if x < K:
                    count=count+1
        b.write("Case #"+str(u)+": "+str(count)+'\n')
        print count
        u=u+1
        q=q-1


if __name__ == "__main__":
    main()
