f = open('inputD.txt')
ff = open('outputD.txt','w')

T= int(f.readline())

for ii in range(T):

    N = int(f.readline())
    a = f.readline().split()
    b = f.readline().split()
    for i in range(N):
        a[i] = float(a[i])
        b[i] = float(b[i])

    if N == 1:
        if a[0] > b[0]:
            ff.write("Case #"+str(ii+1)+": 1 1\n")
        else:
            ff.write("Case #"+str(ii+1)+": 0 0\n")
    if N > 1:
        a.sort()
        b.sort()

        cnt1 = cnt2 = 0
        i= j = N-1
        while(i>-1 and j >-1):
            
            if a[i] > b[j]:
                cnt1+=1
                i-=1
                j-=1
            else:
                j-=1
        i = j = N-1
        while(i>-1 and j>-1):
            if a[i] < b[j]:
                cnt2+=1
                i-=1
                j-=1
            else:
                i-=1
        ff.write("Case #"+str(ii+1)+": "+str(cnt1)+" "+str(N-cnt2)+"\n")
f.close()
ff.close()
