import math
import heapq

with open('C-large.in') as fin:
    T = int(fin.readline().split()[0])
    print(T)
    nStalls = []
    nPeople = []
    for i in range(T):
        dataIn = fin.readline().split()
        nStalls.append(int(dataIn[0]))
        nPeople.append(int(dataIn[1]))

maxima = []
minima = []
for i in range(T):
    n = nStalls[i]
    k = nPeople[i]
    hSlots = []
    dSlots = dict()
    dSlots[n] = 1
    heapq.heappush(hSlots, -n)
    nSlots = 1
    maxSlot = -heapq.heappop(hSlots)
    maxSlotCnt = dSlots[maxSlot]
    while k > maxSlotCnt:
        k = k - maxSlotCnt
        del dSlots[maxSlot]
        r = maxSlot // 2;
        l = r - int(maxSlot % 2 == 0)
        if r in dSlots:
            dSlots[r] += maxSlotCnt
        else:
            dSlots[r] = maxSlotCnt
            heapq.heappush(hSlots, -r)
        if l in dSlots:
            dSlots[l] += maxSlotCnt
        else:
            dSlots[l] = maxSlotCnt
            heapq.heappush(hSlots, -l)
        maxSlot = -heapq.heappop(hSlots)
        maxSlotCnt = dSlots[maxSlot]
    r = maxSlot // 2;
    l = r - int(maxSlot % 2 == 0)
    maxima.append(r)
    minima.append(l)

with open('stall_out.txt', 'w') as fout:
    for i in range(T):
        fout.write('Case #' + str(i + 1) + ': ' +
                   str(maxima[i]) + ' ' +
                   str(minima[i]) + '\n')
    
        
