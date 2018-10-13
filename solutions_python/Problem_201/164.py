
for tests in range(int(input())):

    N,K = (int(i) for i in input().split())

    b = bin(K)

    for i in reversed(b[3:]):

        if i =='1':

            N =(N-1)//2

        else:

            N = N//2

    print ('Case #'+str(tests+1)+': '+str(N//2)+' '+str((N-1)//2))
