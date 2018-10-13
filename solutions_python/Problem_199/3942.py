import string
import Queue
from sets import Set

def Flip(side):
    if side == '-':
        return '+'
    else:
        return '-'

def Check(row):
    for i in row:
        if i == '-':
            return False
    return True

def PancakeFlip(row, num):
    # print
    numPancakes = len(row)
    numFlip = int(num)
    # pancakes = [x for x in row]
    pancakes = row
    q = Queue.PriorityQueue()
    set = Set()
    set.add(pancakes)
    q.put( (0,row) )
    if Check(pancakes):
        return 0
    else:
        while not q.empty():
            (turns,pancakes) = q.get()
            # print " ",row
            for i in xrange(0,1+numPancakes-numFlip):
                newRow = [x for x in pancakes];
                for a in xrange(0,numFlip):
                    # print i+a,
                    newRow[i+a] = Flip(newRow[i+a])
                if Check(newRow):
                    return turns+1
                row = ''.join(newRow)

                # print turns+1,row
                if not row in set:
                    set.add(row)
                    q.put((turns+1,row))
    return -1

if __name__=="__main__":
    input = open('A-small-attempt0.in.txt', 'r')
    testcases = int(input.readline().strip())
    for t in xrange(testcases):
        print "Case #"+str(t+1)+":",
        row, num = input.readline().strip().split()
        turns = PancakeFlip(row,num)
        if turns == -1:
            print "IMPOSSIBLE"
        else:
            print turns
