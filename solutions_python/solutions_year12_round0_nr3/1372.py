#lol2="{0}{1}".format
def main():
    T=int(input())
    for t in range(T):
        astr, bstr= input().split()
        length = len(astr)
        A, Astr, B, Bstr = int(astr), astr, int(bstr), bstr
        perm=[0]*2000000
        ans=0
        #perm.append(Astr)
        for x in range(A,B+1):
            count=1
            xastr, XAstr = str(x), str(x)
            #perm=[]
            perm[x-A]=1
            for _ in range(length-1):
                #xastr = lol2(xastr[-1], xastr[:-1])
                xastr = xastr[-1] + xastr[:-1]
                #lol = int(xastr)
                if (xastr<=Bstr and xastr>=XAstr and (perm[int(xastr)-A]==0)):
                    #print(xastr)
                    perm[int(xastr)-A]=1
                    count+=1
            
            ans=ans + (count*(count-1))//2
        print("Case #{0}: {1}".format(t+1,ans))

main()
