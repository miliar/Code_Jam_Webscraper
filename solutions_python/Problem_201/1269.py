from datetime import datetime
import math
from Queue import PriorityQueue


input_file_path = 'C-small-2-attempt2.in.txt'
#input_file_path = 'C-practice.in.txt'


def bfs(n, k):        # assuming empty array
    if n<0:
        return

    if n>5000 and k>(0.56*n):
        distances.append(0)
        distances.append(0)
        return
    if n>5000 and k>(0.476*n) and k<(0.5*n):
        distances.append(1)
        distances.append(0)
        return

    counter = 0

    queue = PriorityQueue()
    queue.put((0-n, (0,n)))
    done = False
    while not queue.empty() and not done:
        start,end = queue.get()[1]
        index = start + (end-start)/2
        counter = counter + 1
#        print index

        if counter == k:
            distances.append(max([index-start, end-index]))
            distances.append(min([index-start, end-index]))
            done = True

        if(index-1>=start):
            queue.put((start-index+1, (start,index-1)))
        if(end>=index+1):
            queue.put((index+1-end, (index+1,end)))



start = datetime.now()

with open(input_file_path) as f:
    lines = f.read().splitlines()
    for j in range(1,int(lines[0])+1):
        n = long(lines[j].split(' ')[0])
        k = long(lines[j].split(' ')[1])
        distances = []
        bfs(n-1,k)
        print 'Case #' + str(j) + ': ' + str(distances[0]) + ' ' + str(distances[1])


diff = datetime.now() - start
#print diff