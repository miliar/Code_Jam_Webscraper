import heapq


def clever_method_two(n):
    num_stalls, num_people = [int(x) for x in n.split(' ')]

    dist = num_stalls
    distances = [-num_stalls]

    heapq.heapify(distances)
        
    for i in range(num_people):
        distance = heapq.heappop(distances)
        distance *= -1
        mi_tmp, ma_tmp = getMiddle(distance)
        
        heapq.heappush(distances, -ma_tmp)        
        heapq.heappush(distances, -mi_tmp)        
                
    return str(ma_tmp) + ' ' + str(mi_tmp)
    
def getMiddle(num_stalls):
    if num_stalls % 2 == 1:
        x = num_stalls//2
        y = x
    else:
        x = num_stalls//2 - 1
        y = x + 1

    return (x, y)
    
value = int(input())  # read a line with a single integer
for i in range(1, value + 1):
    n = input()
    out = clever_method_two(n)
    print("Case #{}: {}".format(i, out))

    