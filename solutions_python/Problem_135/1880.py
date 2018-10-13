'''str = raw_input("File name: ");'''
str = "A-small-attempt1.in"
fo = open(str, "r");
T = int(fo.readline());
for i in range(T):
    x1 = int(fo.readline()); 
    y1 = []
    for j in range(4):
        for item in fo.readline().strip().split(" "):
            y1.append(int(item))
    y1 = y1[(x1-1)*4:x1*4];
    x2 = int(fo.readline());
    y2 = []
    for j in range(4):
        for item in fo.readline().strip().split(" "):
            y2.append(int(item))
    y2 = y2[(x2-1)*4:x2*4];
    res = set(y1) & set(y2)
    num = len(res)
    if num == 1:
        res = list(res)
        print "Case #%d:" % (i+1), res[0]
    elif num > 1:
        print "Case #%d: Bad magician!" % (i+1) 
    elif num == 0:
        print "Case #%d: Volunteer cheated!" % (i+1) 

