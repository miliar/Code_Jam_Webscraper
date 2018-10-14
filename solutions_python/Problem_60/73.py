def go():
    infile=open('in.txt')
    c=int(infile.readline())
    for case in range(c):
        n,k,b,t=[int(x) for x in infile.readline().split()]
        starts=[int(x) for x in infile.readline().split()]
        speeds=[int(x) for x in infile.readline().split()]
        starts.reverse()
        speeds.reverse()



        print 'Case #%d: %s'%(case+1,solve(n,k,b,t,speeds,starts))




    infile.close()


def solve(n,k,b,t,speeds,starts):
    can=[]
    for x in range(n):
        if b-t*speeds[x]-starts[x]<=0:
            can.append(1)
        else:
            can.append(0)
    if can.count(1)<k:
        return 'IMPOSSIBLE'
    
    swaps=0
    aheads=0
    done=0
    thischick=0
    while done<k:
        if can[thischick]:
            swaps+=aheads
            done+=1
        else:
            aheads+=1
        thischick+=1
        
    return swaps
        
