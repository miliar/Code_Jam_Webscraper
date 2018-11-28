import bisect

def mm(inp, div):
        imin = inp/div/1.1
        imax = inp/div/0.9
        
        #return (imin,imax)
        if imin != int(imin):
                imin = int(imin) + 1
        else:
                imin = int(imin)

        imax = int(imax)
        return(imin,imax)
                

T = int(input())


for tc in range(0, T):
        row = input().split(' ')
        N = int(row[0])
        P = int(row[1])
        R = [int(x) for x in input().split(" ")]
        
        #print (R)
        
        Q=[]
        Qi=[]
        Qc=[]
        
        for n in range(0, N):
                Qtemp = [float(x) for x in input().split(" ")]
                Qtemp.sort()
                #print (Qtemp)
                for p in range(P-1, -1, -1):
                        Qtemp[p] = mm(Qtemp[p],R[n])
                        if Qtemp[p][0] > Qtemp[p][1]:
                                Qtemp.pop(p)
                        
                Q.append(Qtemp)
                Qi.append(0)
                Qc.append(len(Qtemp))

        #print(Q)
        answer = 0
        xx=0
        while True:
                curmin = -1
                curmax = 99999999

                realmin = curmax
                minind = -1
                setbreak = False
                for n in range(0, N):
                        if Qi[n] >= Qc[n]:
                                setbreak = True
                                break
                        
                        if Q[n][Qi[n]][0] < realmin:
                                realmin = Q[n][Qi[n]][0]
                                minind = n
                                
                        if Q[n][Qi[n]][0] > curmin:
                                curmin = Q[n][Qi[n]][0]

                        if Q[n][Qi[n]][1] < curmax:
                                curmax = Q[n][Qi[n]][1]

                if setbreak:
                        break

                if curmin>curmax :
                        Qi[minind] = Qi[minind] + 1
                else:
                        for n in range(0, N):
                                Qi[n] = Qi[n] + 1
                        answer = answer + 1

                xx = xx+1
        #print (xx)
                        
        
        
        print ('Case #' + str(tc+1) + ': ' + str(answer))
