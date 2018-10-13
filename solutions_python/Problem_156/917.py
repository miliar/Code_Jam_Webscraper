import heapq

def dp(pq, total):
    highest = -pq[0]
    if highest < 4:
        total += highest
        return total

    #Scenario 1: Split largest value in half
    pq1 = pq[:]
    heapq.heappop(pq1)
    heapq.heappush(pq1, -highest/2)
    heapq.heappush(pq1, -(highest-highest/2))
    total1 = dp(pq1, total+1)

    #Scenario 2: Everyone eats
    pq2 = [x+1 for x in pq if x+1 < 0]
    heapq.heapify(pq2)
    total2 = dp(pq2, total+1)

    #Scenario 3: Split largest value into thirds
    pq3 = pq[:]
    heapq.heappop(pq3)
    heapq.heappush(pq3, -highest/3)
    heapq.heappush(pq3, -highest/3)
    heapq.heappush(pq3, -(highest-2*highest/3))
    total3 = dp(pq3, total+2)

    return min(total1, total2, total3)


fin = file("B-small-attempt1.in.txt", "rU")
fout = file("B-small-attempt1.out.txt", "w")

nruns = int(fin.readline().strip())
for i in xrange(nruns):
    line = fin.readline().strip().split()

    diners = int(line[0])

    plates = [-int(x) for x in fin.readline().strip().split()]
    heapq.heapify(plates)
    
    result = dp(plates, 0)
    
    strout = "Case #" + str(i+1) + ": " + str(result) + "\n"
    #print strout
    fout.write(strout)
fin.close()
fout.close()
