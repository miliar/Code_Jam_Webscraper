from heapq import heappush, heappop

#--- READ INPUT ---#
inp = open('C-small-2-attempt1.in', 'r')
#inp = open('A-large.in', 'r')
#inp = open('test.in', 'r')
o = open('output_small_2.txt', 'w')

test_cases = int(inp.readline())
for i in range(test_cases):
    line = inp.readline()[:-1].split(' ')
    n = int(line[0])
    k = int(line[1])
    print(i)

    #--- SOLUTION ---#
    #l = [n]
    heap = [-n]
    for j in range(k):
        '''
        maximum = max(l)
        l.remove(maximum)
        '''
        maximum = -heappop(heap)
        new1 = int((maximum / 2) - 0.5)
        new2 = maximum - new1 -1
        if new2 != 0:
            heappush(heap, -new2)
        if new1 != 0:
            heappush(heap, -new1)

    res = [max(new1, new2), min(new1, new2)]
    #--- WRITE OUTPUT ---#
    s = 'Case #' + str(i+1) + ': ' + str(res[0]) + ' ' + str(res[1])
    o.write(s + '\n')
inp.close()
o.close()
