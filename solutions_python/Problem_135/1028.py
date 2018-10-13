import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    f = open("a.out", 'w')

    for i in range(T):
        r1 = int(sys.stdin.readline())
        for j in range(1, 5):
            if j == r1:
                row = sys.stdin.readline().split()
                r1_set = set(row)
            else:
                sys.stdin.readline()

        r2 = int(sys.stdin.readline())
        for j in range(1,5):
            if j == r2:
                row = sys.stdin.readline().split()
                r2_set = set(row)
            else:
                sys.stdin.readline()
        
        intersect = r1_set.intersection(r2_set)
        
        if len(intersect) == 0:
            f.write("Case #%d: Volunteer cheated!\n" %(i+1))
        elif len(intersect) == 1:
            el = intersect.pop()
            f.write("Case #%d: %s\n" %(i+1, el))
        else:
            f.write("Case #%d: Bad magician!\n" %(i+1))
    f.close()
