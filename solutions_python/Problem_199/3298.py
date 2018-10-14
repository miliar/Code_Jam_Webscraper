from queue import PriorityQueue 

def isdone(state):
    return "-" not in state

def searchmin(cakes, k):
    searched = set()
    q = PriorityQueue()
    q.put((0, cakes))
    while not q.empty():
        m, state = q.get()
        if isdone(state):
            return m
        searched.add(state)
        i = 0
        for i in range(len(state)-k+1):
            nlist = list(state)
            for j in range(k):
                nlist[i+j] = "+" if nlist[i+j] == "-" else "-"
            newstate = "".join(nlist)
            if newstate not in searched:
                q.put((m+1,newstate))
    return -1

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    cakes, k = input().split(" ")
    k = int(k)
    m = searchmin(cakes, k)
    if m < 0:
        print("Case #{}: IMPOSSIBLE".format(i))
    else:
        print("Case #{}: {}".format(i, m))
