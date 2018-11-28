t = int(input())

def cango(start, end, horses, distance):
    d = 0
    current = start
    while(current != end):
        d += distance[(current, current + 1)]
        current += 1
    if horses[start][0] < d:
        return (False, 0)
    else:
        return (True, d/horses[start][1])
        

for test in range(t):
    n, q = map(int, input().split())
    horses = [(10**18, 10**18)]
    for i in range(n):
        e, s = map(int, input().split())
        horses.append((e,s))
    distance = {}
    for i in range(n):
        numbers = list(map(int, input().split()))
        for item in numbers:
            if item != -1:
                distance[((i + 1), (i + 2))] = item
    u, v = map(int, input().split())
    inf = 10**18
    answer = [inf]*(n + 1)
    answer[u] = 0
    answer[u + 1] = distance[(u, u + 1)]/horses[u][1]
    for rat in range(u + 2, v + 1):
        counter = 1
        while True:
            fnode = rat - counter
            if(answer[fnode] == inf):
                break
            tempresult = cango(fnode, rat, horses, distance)        
            if(tempresult[0]):
                answer[rat] = min(answer[rat], tempresult[1] + answer[fnode])
            counter += 1
    print("Case #" + str(test + 1)+": "+str(answer[v]))
                
