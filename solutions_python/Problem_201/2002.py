# import time
from bisect import bisect
import math
def BathroomCount(count, noPeople):
    if count<50:
        a=1    
    elif float(noPeople) > 0.6 * count:
        return [0,0]
    elif (count%2==1 and (noPeople == math.floor(count/2) or noPeople == math.ceil(count/2))) or (count%2==0 and (noPeople == count/2 or noPeople == (count/2)-1 or noPeople == (count/2)+1)):
        return [1,0]
    elif noPeople == 1 and count%2==0:
        return [count/2, (count/2) - 1]
    elif noPeople == 1 and count%2==1:
        return [math.floor(count/2), math.floor(count/2)]
    # elif float(noPeople) > 0.6 * count:
    #     return [0, 0] 


    stalls = ['1'] + ['0'] * count + ['1']
    #print(stalls)
    for p in range(0, noPeople):    
        

        minLR = 0
        maxLR = 0

        dist=[]
        occupied = [i for i,x in enumerate(stalls) if x=='1']
        for i in range(1,len(stalls)-1):
            j=bisect(occupied,i)
            if i == occupied[j-1]:
                dist.append([-1,-1])
            else:
                dist.append([i-occupied[j-1]-1, occupied[j]-i-1])




        distances = GetDistances2(stalls)
        minDist = [min(s) for s in distances]
        candidates = [i for i,x in enumerate(minDist) if x==max(minDist)]

        if len(candidates) == 1:
            stalls[candidates[0] + 1] = '1'
            maxLR = max(distances[candidates[0]])
            minLR = min(distances[candidates[0]])
        else:
            maxDist = [max(distances[s]) for s in candidates]
            newCandidates = [i for i,x in enumerate(maxDist) if x==max(maxDist)]
            maxLR = max(distances[candidates[newCandidates[0]]])
            minLR = min(distances[candidates[newCandidates[0]]])
            stalls[candidates[newCandidates[0]] + 1] = '1'
        
        #print(stalls)
    
    return [maxLR, minLR]

def GetDistances2(stalls):
    dist=[]
    occupied = [i for i,x in enumerate(stalls) if x=='1']
    for i in range(1,len(stalls)-1):
        j=bisect(occupied,i)
        if i == occupied[j-1]:
            dist.append([-1,-1])
        else:
            dist.append([i-occupied[j-1]-1, occupied[j]-i-1])
        
    #print(dist)
    return dist


# def GetDistances(stalls):
#     dist = []
#     for i in range(1, len(stalls)-1):
#         if stalls[i] == '0':
#             countLeft = 0
#             for j in range(0, i):
#                 countLeft += 1
#                 if stalls[j] == '1':
#                     countLeft = 0
            
#             countRight = 0
#             for k in range(len(stalls)-1, i, -1):
#                 countRight += 1
#                 if stalls[k] == '1':
#                     countRight = 0

#             dist.append([countLeft, countRight])
#         else:
#             dist.append([-1 , -1])
#     return dist

t = int(input())  # read a line with a single integer
# start_time = time.time()
for i in range(1, t + 1):
    
    n, m = [int(s) for s in input().split(" ")]
    answer1, answer2 = [int(s) for s in BathroomCount(n, m)]
    
    print("Case #{}: {} {}".format(i, answer1, answer2))

# print("--- %s seconds ---" % (time.time() - start_time))