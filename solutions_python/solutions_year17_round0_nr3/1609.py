import heapq

def calculateS(stalls, N):
    for i in range(1, N+1):
        stalls[i] = [False, i - 1, N - i]

def updateStall(stalls, index):
    stalls[index][0] = True
    left = index - 1
    right = index + 1
    while not stalls[left][0]:
        stalls[left][2] = index - left - 1
        left -= 1
        
    while not stalls[right][0]:
        stalls[right][1] = right - index - 1
        right += 1

def minStall(stalls, N):
    first = -1
    second = -1
    chosen = 0
    for i in range(1, N+1):
        if not stalls[i][0]:
            minimum = min(stalls[i][1], stalls[i][2])
            maximum = max(stalls[i][1], stalls[i][2])
            if minimum > first:
                first = minimum
                second = maximum
                chosen = i
            elif minimum == first and maximum > second:
                first = minimum
                second = maximum
                chosen = i
    updateStall(stalls, chosen)
    return chosen

fileName = "C-small-2-attempt1.in"
f = open(fileName, 'r')

outputName = "C-small2-1-out.txt"
output = open(outputName, 'w')

line = f.readline()
T = int(line)

for t in range(T):
    res = ""
    line = f.readline().split()
    N = int(line[0])
    K = int(line[1])
    

    heap = [-N]
    heapq.heapify(heap)
    #print(heap)
    for i in range(K):
        top = heapq.heappop(heap)
        top = top * -1
        if top % 2 == 1:
            e1 = (top - 1)/2
            e1 = e1 * -1
            e2 = e1
        else:
            e1 = top/2
            e2 = e1 - 1
            e1 = e1 * -1
            e2 = e2 * -1
        heapq.heappush(heap, e1)
        heapq.heappush(heap, e2)
    e1 = int(e1 * -1)
    e2 = int(e2 * -1)
    res = "{} {}".format(max(e1, e2), min(e1,e2))
    # stalls = [None for i in range(N + 2)]
#     stalls[0] = [True, 0, 0]
#     stalls[N + 1] = [True, 0, 0]
#
#     calculateS(stalls, N)
#     for i in range(K):
#         chosen = minStall(stalls, N)
#
#     res = "{} {}".format(max(stalls[chosen][1], stalls[chosen][2]), min(stalls[chosen][1], stalls[chosen][2]))
#
    print("Case #{}: {}".format(t+1, res))
    output.write("Case #{}: {}".format(t+1, res))
    output.write("\n")

output.close()