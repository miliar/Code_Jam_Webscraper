import copy
import heapq
cases = []

with open('C-small-2-attempt0.in','r') as infile:
    for row in infile:
        paras = row.strip().split(' ')
        if len(paras) > 1:
            cases.append((paras[0],paras[1]))

def stall_finder(num,K):
    heap = [(-num,num)]
    heapq.heapify(heap)
    mi,ma = 0,0
    for i in range(K-1):
        #print heap
        k,cur = heapq.heappop(heap)
        if cur%2 == 0:
            x,y = cur/2-1,cur/2
            heapq.heappush(heap,(-x,x))
            heapq.heappush(heap,(-y,y))
        else:
            x,y = (cur-1)/2,(cur-1)/2
            heapq.heappush(heap,(-x,x))
            heapq.heappush(heap,(-y,y))
    #print heap
    k,cur = heapq.heappop(heap)
    #print cur
    if cur % 2 == 0:
        x, y = cur / 2 - 1, cur / 2
    else:
        x, y = (cur - 1) / 2, (cur - 1) / 2
    mi = min(x,y)
    ma = max(x,y)
    return mi,ma


ans = []
test = []
for i,case in enumerate(cases):
    test.append(case[0])
    #print case
    mi,ma = stall_finder(int(case[0]),int(case[1]))
    ans.append('Case #'+str(i+1)+': '+str(ma)+' '+str(mi))


with open('C-small-2-attempt0.out','w') as outfile:
    for row in ans:
        outfile.write(row+'\n')

with open('infile.txt','w') as outfile:
    for row,roww in zip(test,ans):
        outfile.write(row+' '+roww+'\n')
