import sys

numTests = int(sys.stdin.readline())
for i in range (0,numTests):
    row1 = int(sys.stdin.readline());
    for j in range(0,row1-1):
        sys.stdin.readline()
    row1Content = set(sys.stdin.readline().split());
    for j in range(row1,4):
        sys.stdin.readline()

    row2 = int(sys.stdin.readline());
    for j in range(0,row2-1):
        sys.stdin.readline()
    row2Content = set(sys.stdin.readline().split());
    for j in range(row2,4):
        sys.stdin.readline()
    interection = row1Content.intersection(row2Content)
    count = len(interection)
    if count==0:
        print "Case #"+str(i+1)+": Volunteer cheated!"
    elif count==1:
        print "Case #"+str(i+1)+":",list(interection)[0]
    else:
        print "Case #"+str(i+1)+": Bad magician!"
