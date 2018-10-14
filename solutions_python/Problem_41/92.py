INPUT = 'B-large.in'
OUTPUT = 'B-large.out'

def findNext(a):

    number = a
    numbers = []
    for i in xrange(len(str(a))):
        n = a % 10
        a -= n
        a = a / 10
        numbers.append(n)
    i = 0
    queue = []
    ready = False
    while not ready:
        queue.append(numbers[i])

#        print 'appending', numbers[i]
        if i == len(numbers)-1:
            break
        for number in queue:
            if numbers[i+1] < number:
                queue.append(numbers[i+1])
                pivot = numbers[i+1]
                ready = True
                break
        i += 1
#    print queue
    if not ready: #i == len(numbers)-1 and :
        starting = []
        queue.append(0)
        queue.sort()
        for i in xrange(len(queue)):
            if queue[i] > 0:
                starting.append(queue[i])
                queue.pop(i)
                break
        for i in queue:
            starting.append(i)
    else:
        starting = numbers[i+1:]
        starting.reverse()
        queue.sort()
        for i in xrange(len(queue)):
            if queue[i] > pivot:
                starting.append(queue[i])
                queue.pop(i)
                break
        for i in queue:
            starting.append(i)
    newNumber = 0
    starting.reverse()
    for i in xrange(len(starting)):
        newNumber += starting[i]*(10**i)
    return newNumber
        
        
    
    
        


if __name__=='__main__':

    input = open(INPUT)
    output = open(OUTPUT, 'w')
    N = int(input.readline().strip())
    for i in range(N):
        a = int(input.readline().strip())

        number = findNext(a)
        output.write('Case #%d: %d\n' % (i+1, number))
        #print 'Case #%d: %d' % (i+1, number)
    output.close()

#print findNext(33)
