file = open("C-small.in", "r")
out = open("C-small.out", "w")
T = int(file.readline())

for ncase in xrange(T):
    R, k, N = map(int, file.readline().strip().split(" "))
    queue = map(int, file.readline().strip().split(" "))

    auxQueue = []
    money = 0
    for _ in xrange(R):
        people = 0
        while len(queue) > 0 and queue[0] <= k - people:
            people += queue[0]
            auxQueue.append(queue.pop(0))
        money += people
        queue.extend(auxQueue)
        del auxQueue[:]


    out.write("Case #%s: %s\n" % (ncase+1, money) )




file.close()
out.close()
