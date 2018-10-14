from queue import PriorityQueue
 
#def floyd_warshall(graph):
#    for n1 in range(len(graph)):
#        for n2,weight in enumerate(graph[n1]):
            

def djikstras(graph,start, end):
    queue = PriorityQueue()
    queue.put((0,start))
    has_seen = set()
    has_seen.add(start)
    while not queue.empty():
        (weight,node) = queue.get()
        has_seen.add(node)
        if node == end:
            return weight
        for nn,addweight in enumerate(graph[node]):
            if addweight != -1 and  nn not in has_seen:
                newweight = weight + addweight
                queue.put((newweight,nn))
               
    return -10000
    
def djikstras_horses(graph,start,max_dis,horse_speed):
    queue = PriorityQueue()
    queue.put((0,start))
    has_seen = set()
    has_seen.add(start)
    out_weights = [-1]*len(graph)
    while not queue.empty():
        (weight,node) = queue.get()
        has_seen.add(node)
        if weight > max_dis:# equals?
            continue
        out_weights[node] = weight
        for nn,addweight in enumerate(graph[node]):
            if addweight != -1 and  nn not in has_seen:
                newweight = weight + addweight
                queue.put((newweight,nn))
               
    return [-1 if dis == -1 else dis/horse_speed for dis in out_weights]

T = int(input())
for case in range(T):
    vals = input().split()
    N,Q = [int(v) for v in vals]
    
    horses = [[int(v) for v in input().split()] for _ in range(N)]
    routes_dists = [[int(v) for v in input().split()] for _ in range(N)]
    analyse_routes = [[int(v) for v in input().split()] for _ in range(Q)]
    
    processed_routes = []
    for node,[horse_dis,horse_speed] in enumerate(horses):
        processed_routes.append(djikstras_horses(routes_dists,node,horse_dis,horse_speed))
    #print(processed_routes)
    outsdis = []
    for [start,end] in analyse_routes:
        outsdis.append(djikstras(processed_routes,start-1,end-1))
    
    disstr = " ".join("%.6f"%v for v in outsdis)
    print("Case #%d: %s"%(case+1,disstr))
        
    