'''
Created on Mar 19, 2016

@author: elmoatasem
'''

import math
def getNearestPow2(N):
    nextP2 = pow(2, math.floor(math.log(N)/math.log(2)));
    return int(nextP2)
   


def getMaxSlotBoundriesIndex(slots,slotSizes):
    maxSpaceIndex = -1 
    maxSpace = -1 
    for i in range(len(slotSizes)):
        if(slotSizes[i] > maxSpace):
            maxSpaceIndex = i
            maxSpace = slotSizes[i]
            
    return maxSpaceIndex
    
    
def getLastSlotIndex(N,K):
    
    slots = [(0,N + 1)]
    slotSizes = [N]
    
    stalls = ['.'] * (N + 2)
    stalls[0] = 'o'
    stalls[N + 1] = 'o'
     
    print slots ,slotSizes
    print stalls
    
    Ls = -1
    Rs = -1
    
    while(K <> 0):
        maxSpaceIndex = getMaxSlotBoundriesIndex(slots,slotSizes)
        (start,end) = slots[maxSpaceIndex]
        del slots[maxSpaceIndex]
        del slotSizes[maxSpaceIndex]
        print(len(slots))
        mid = (start + (end - 1)) / 2
        if((start + (end - 1)) % 2 == 0):
            mid = mid
        else:
            mid = mid + 1
        stalls[mid] = 'o'
        Ls = (mid - start - 1)
        Rs = ((end - 1) - mid)
        slotSizes.append((mid - start - 1))
        slots.append((start,mid))
        slotSizes.append(((end - 1) - mid))
        slots.append((mid,end))

        K -= 1
        
        print slots ,slotSizes
        print stalls
        print max(Ls,Rs),min(Ls,Rs)
        
    return " ".join([str(max(Ls,Rs)),str(min(Ls,Rs))])
        
    
    
def solve(N,K):
    nearKP2 = getNearestPow2(K)
    slotIndex = (K % nearKP2)

    maxSlotCut = -1
    averageSlotCut = -1
    nearKP2 = nearKP2
    occupiedSlotsCount = 0
    n = 0
    if(nearKP2 > 1):
        n = int(math.floor(math.log(nearKP2 / 2)/math.log(2)))
        occupiedSlotsCount = (1 - 2**(n + 1)) / (1 - 2)
    remSlotsCount = N - occupiedSlotsCount
    
    if(N % nearKP2 == 0):
        maxSlotCut = (N / nearKP2)
        averageSlotCut = (N / nearKP2)
    else :
        maxSlotCut = (N / nearKP2) + (N % nearKP2)
        averageSlotCut = (N / nearKP2)
        
        
#     print "nearP2",nearKP2
#     print "n",n 
#     print "occupiedSlots",occupiedSlotsCount
#     print "slotIndex",slotIndex
#     print "remSlots",remSlotsCount
#     print N,nearKP2
#     print 'maxSlotCut',maxSlotCut
#     print 'averageSlotCut',averageSlotCut
#     print"Q",(N / nearKP2)
#     print"R",(N % nearKP2)
    R = (N % nearKP2)
    arr = [(N / nearKP2)]
    arr.extend([averageSlotCut] * (nearKP2 - 1))   
    for i in range(R):
        arr[i] += 1
    qotDist = occupiedSlotsCount / nearKP2
    remDist = occupiedSlotsCount % nearKP2
    arr = list(map(lambda x: x - qotDist, arr))
    for i in range(remDist):
        arr[i] -= 1
    
    arr.sort(reverse=True)
#     print arr
    area = arr[slotIndex]
#     print 'area',area
    Ls = 0
    Rs = 0
    if(area != 0):
        start = 0
        end = area + 1
        mid = area / 2
        Ls = (mid - start)
        Rs = ((end - 1) - mid - 1)
#     print Ls,Rs
#     print max(Ls,Rs),min(Ls,Rs) 
        
    
#     print"qotDist",qotDist
#     print"remDist",remDist
    return " ".join([str(max(Ls,Rs)),str(min(Ls,Rs))]) 

f_r = open('C-small-2-attempt0.in',"r")
# f_r = open('C.in',"r")
n_test=int(f_r.readline().strip()) 
f_w = open("C_Small_Output_2.out", "w")
result = ""
for i in range(n_test):
    N,K =  map(int,f_r.readline().split())
    print N,K
    result = solve(N,K)
    print result

    output_str='Case #{itr}: {res}'.format(itr=(i+1),res=result)
    f_w.write(output_str+'\n')
    
f_r.close()

