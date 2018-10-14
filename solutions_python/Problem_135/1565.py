import sys

N = int(sys.stdin.readline())

for i in range(N):
    n = int(sys.stdin.readline())
    for j in range(4):
        line = sys.stdin.readline()
        if n == j+1:
            arr1 = line[:-1].split()
    n = int(sys.stdin.readline())
    for j in range(4):
        line = sys.stdin.readline()
        if n == j+1:
            arr2 = line[:-1].split()

    inter = list(set(arr1).intersection(set(arr2)))
    print "Case #%d:"%(i+1),
    if len(inter) == 0:
        print "Volunteer cheated!"
    elif len(inter) == 1:
        print "%s"%inter[0]
    else:
        print "Bad magician!"
