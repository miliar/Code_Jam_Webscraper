import sys

def main():
    fin = open(sys.argv[1])

    cases = int(fin.readline().strip())
    for c in range(cases):
        ans1 = int(fin.readline().strip()) - 1
        line1 = []
        for i in range(4):
            line = fin.readline().strip()
            if i == ans1:
                line1 = line
                
        ans2 = int(fin.readline().strip()) - 1
        line2 = []
        for i in range(4):
            line = fin.readline().strip()
            if i == ans2:
                line2 = line
                
        cards1 = [int(n) for n in line1.split()]
        cards2 = [int(n) for n in line2.split()]
        intersect = list(set(cards1) & set(cards2))
        
        if len(intersect) == 0:
            print "Case #%d: Volunteer cheated!" % (c + 1)
        elif len(intersect) == 1:
            print "Case #%d: %d" % (c + 1, intersect[0])
        else:
            print "Case #%d: Bad magician!" % (c + 1)
        

if __name__ == "__main__":
    main()
