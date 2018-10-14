f = open("../magic.in", "r")
w = open("../magic.out", "w")
T = int(f.readline())

for i in range(1, T + 1):
    print "Case #" + str(i) + ":",
    a = int(f.readline())
    for j in range(1, 5):
        if j == a:
            first_set = set(map(int, f.readline().split()))
        else:
            f.readline()
            
    a = int(f.readline())
    for j in range(1, 5):
        if j == a:
            first_set &= set(map(int, f.readline().split()))
        else:
            f.readline()
    if len(first_set) == 0:
        print "Volunteer cheated!"
    elif len(first_set) == 1:
        print list(first_set)[0]
    else:
        print "Bad magician!" 
