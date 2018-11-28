import math

T = int(raw_input())


for tc in range(0, T):
        input = raw_input().split(' ')

        N = int(input[0])
        K = int(input[1])

        arr=[]
        for n in range(0, N):
                input = raw_input().split(' ')
                R = int(input[0])
                H = int(input[1])

                arr.append([R,H])
        arr = sorted(arr,key=lambda arr:arr[0], reverse=True)

        dyn=[]
        for k in range(0, K):
                dyn_sub=[]
                for n in range(0, N):                
                        dyn_max=0
                        R=arr[n][0]
                        H=arr[n][1]
                        if k==0:
                                dyn_max=(math.pi*R*R)+(2.0*math.pi*R*H)

                        elif k<=n:
                                dyn_max=dyn[k-1][n-1]+(2.0*math.pi*R*H)

                        if n>0:
                                dyn_max=max(dyn_max,dyn_sub[n-1])
                                
                        dyn_sub.append(dyn_max)
                dyn.append(dyn_sub)
        


#        for k in range(0, K):
#                print dyn[k]

        
        print 'Case #' + str(tc+1) + ': ' + '%.9lf' % (dyn[K-1][N-1]) 
