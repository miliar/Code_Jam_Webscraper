import sys
from sets import Set

C = int(sys.stdin.readline().rstrip('\n'))

for c in range(1, C+1):
    first = int(sys.stdin.readline().rstrip('\n'))
    arr1 = Set()
    for r in range(4):
        if first - 1 == r :
            li = sys.stdin.readline().rstrip('\n').split()
            cand1 = [int(e) for e in li]
            arr1 = Set(cand1)
        else:
            sys.stdin.readline()
        
    second = int(sys.stdin.readline().rstrip('\n'))
    arr2 = Set()
    for r in range(4):
        if second -1 == r:
            li = sys.stdin.readline().rstrip('\n').split()
            cand2 = [int(e) for e in li]
            arr2 = Set(cand2)
        else:
            sys.stdin.readline()

    intersec = arr1.intersection(arr2)
    
    size = len(intersec)
    if size == 1:
        print "Case #%d: %d"%(c, intersec.pop())
    if size == 0:
        print "Case #%d: %s"%(c, 'Volunteer cheated!')
    if size > 1:
        print "Case #%d: %s"%(c, 'Bad magician!')
        
        
