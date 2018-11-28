import queue

def bathroomStalls(n, k):
    if n == k:
        return 0, 0
    stallQueue = queue.PriorityQueue(n)
    stallQueue.put((-n, n))
    openStalls, newStalls, otherStalls = 0, 0, 0
    for i in range(0, k):
        openStalls = stallQueue.get()[1] - 1
        newStalls = openStalls // 2
        otherStalls = openStalls - newStalls
        stallQueue.put((-otherStalls, otherStalls))
        stallQueue.put((-newStalls, newStalls))

    return otherStalls, newStalls

def main():
    t = int(input())
    for i in range(1, t + 1):
        n, m = [int(s) for s in input().split(" ")]
        y, z = bathroomStalls(n ,m)
        print ("Case #{}: {} {}".format(i, y, z))

main()