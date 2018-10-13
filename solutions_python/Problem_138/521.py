import sys
import copy

f=open(sys.argv[1])
T=int(f.readline())
case=1
while case<T+1:
    N=int(f.readline())
    Nao=[]
    for r in f.readline().split():
        Nao.append(float(r))
    Nao.sort()
    #print Nao

    Ken=[]
    for r in f.readline().split():
        Ken.append(float(r))
    Ken.sort()
    #print Ken

    #Deceitful War
    dwpoint=0
    dwNao=copy.copy(Nao)

    for i in xrange(N):
        flag=True
        #print dwNao,dwpoint
        for j in xrange(N-i):
            if Ken[i]<dwNao[j]:
                del dwNao[j]
                flag=False
                dwpoint+=1
                break

        if flag:
            del dwNao[0]

    #War
    wpoint=0
    wKen=copy.copy(Ken)

    for i in xrange(N):
        flag=True
        #print wKen,wpoint
        for j in xrange(N-i):
            if Nao[i]<wKen[j]:
                del wKen[j]
                flag=False
                break
        if flag:
            del wKen[0]
            wpoint+=1


    print "Case #"+str(case)+": %d %d"%(dwpoint,wpoint)
    case+=1
