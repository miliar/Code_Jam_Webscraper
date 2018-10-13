from queue import PriorityQueue


def chooseStalls(numStalls, peopleLeft, pq):
    pq.put((0, (0, numStalls - 1)))
    sizeLeft = 0
    sizeRight = 0
    if (peopleLeft / numStalls) > 0.65:
        return 0, 0
    for i in range(peopleLeft):
        indices = pq.get()[1]
        beg = indices[0]
        end = indices[1]
        toInsert = ((end - beg) // 2) + beg
        sizeLeft = toInsert - beg
        sizeRight = end - toInsert
        if (sizeLeft > 0):
            pq.put((-sizeLeft, (beg, toInsert - 1)))
        if (sizeRight > 0):
            pq.put((-sizeRight, (toInsert + 1, end)))
    return sizeLeft, sizeRight

t = int(input())
for i in range(1, t+1):
    numStalls, numPeople = [int(s) for s in input().split(" ")]
    pq = PriorityQueue()
    stallLeft, stallRight = chooseStalls(numStalls, numPeople, pq)
    print("Case #{}: {} {}".format(i, max(stallLeft, stallRight), min(stallLeft, stallRight)))