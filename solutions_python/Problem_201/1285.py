import heapq

ans = []
with open("C-small-2-attempt2.in") as f:
    content = f.readlines()

content = [x.strip() for x in content]

t = int(content[0])

def split(number):
    """splitting the numbers"""
    if number == 0:
        return [0, 0]
    if number%2 == 0:
        no1 = int(number/2)
        no2 = int(number/2 - 1)
    else:
        no1 = int((number-1)/2)
        no2 = int((number-1)/2)
    return [no1, no2]


for i in range(t):

    n, k = list(map(int, content[i+1].split(' ')))

    heap = []
    heapq.heappush(heap, (-1)*n)

    for j in range(k-1):
        max_now = heapq.heappop(heap)  
        splitted = split((-1)*max_now)
        heapq.heappush(heap, (-1)*splitted[0])
        heapq.heappush(heap, (-1)*splitted[1])

    max_now = split((-1)*heapq.heappop(heap))

    ans.append(max_now)

fw = open("C-small-2-attempt2.out", 'w')

for i, x in enumerate(ans):
    fw.write("Case #{0}: {1} {2}\n".format(i+1, x[0], x[1]))