import sys
fname = sys.argv[1]
with open(fname) as f:
    cases = int(f.readline())
    for i in range(cases):
        ansrow1 = int(f.readline())        
        row1 = []
        for j in range(ansrow1):
            row1 = map(lambda x:int(x),f.readline().split())
        for j in range(4-ansrow1):
            f.readline()
        ansrow2 = int(f.readline())        
        row2 = []
        for j in range(ansrow2):
            row2 = map(lambda x:int(x),f.readline().split())
        for j in range(4-ansrow2):
            f.readline()
        a = filter(lambda x: x in row2,row1)
        if len(a)==1:
            print("Case #%s: %s"%(i+1,a[0]))
        elif len(a)==0:
            print("Case #%s: Volunteer cheated!"%(i+1,))
        else:
            print("Case #%s: Bad magician!"%(i+1,))
        
