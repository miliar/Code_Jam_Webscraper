

try:
    import Queue as Q 
except ImportError:
    import queue as Q


class BathRoom(object):
    def __init__(self, entrance, exit):
        self.entrance = entrance
        self.exit = exit
        return

    def __cmp__(self, other):
        n = (other.exit - other.entrance) - (self.exit - self.entrance)
        if n != 0:
            return n
        return self.exit - other.exit


def clear_queue(myQueue):
    while not myQueue.empty():
        try:
            myQueue.get(False)
        except Empty:
            continue
        q.task_done()

def makeCheckAvailability():

    currentUseBathroom = None
    queue = None

    with open("C-small-1-attempt1.in", mode='r') as fp:
        testCase = int(fp.readline())
        count = 0
        for line in fp:
            data = line[:-1].split(" ")
            numberOfBathrooms = long(data[0])
            peopleToUseBathroom = long(data[1])
            queue = Q.PriorityQueue()
            queue.put(BathRoom(0, numberOfBathrooms+1))

            for i in range(peopleToUseBathroom - 1):
                currentUseBathroom = queue.get()
                position = (currentUseBathroom.exit + currentUseBathroom.entrance) // 2
                queue.put(BathRoom(currentUseBathroom.entrance, position))
                queue.put(BathRoom(position, currentUseBathroom.exit))

            currentUseBathroom = queue.get()

            result = (currentUseBathroom.exit + currentUseBathroom.entrance) / 2
            x = max(result - currentUseBathroom.entrance - 1, currentUseBathroom.exit - result - 1)
            y = min(result - currentUseBathroom.entrance - 1 , currentUseBathroom.exit - result - 1)
            count = count + 1
            print("Case #{}: {} {}".format(count,x, y))



if __name__ == "__main__":
    makeCheckAvailability()
   


