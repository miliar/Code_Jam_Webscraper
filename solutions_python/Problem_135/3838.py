import sys

f = open(sys.argv[1], 'r')
tests = int(f.readline())

for i in range(tests):
    a = []
    b = []
    r = int(f.readline())
    for j in range(4):
        line = f.readline()
        if r == j + 1:
            a = map(int, line.split(" "))
    r = int(f.readline())
    for j in range(4):
        line = f.readline()
        if r == j + 1:
            b = map(int, line.split(" "))
    cnt = 0
    n = 0
    
    print "Case #%d:" % (i + 1),
    for i in range(4):
        for j in range(4):
            if a[i] == b[j]:   
                n = a[i]
                cnt += 1
    if cnt == 0:
        print "Volunteer cheated!"
    elif cnt > 1:
        print "Bad magician!"
    else:
        print n


