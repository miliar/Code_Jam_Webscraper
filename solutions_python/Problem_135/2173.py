f = open("A-small-attempt0.in", "r")
s = open("output.txt","w")
t = int (f.readline())
for i in range(0,t):
    x  = int(f.readline())
    for j in range(0,4):
        a = f.readline()
        if x==j+1:
            x1 = a.rstrip('\n').split(' ')
    y = int(f.readline())
    for j in range(0,4):
        a = f.readline()
        if y == j+1:
            y1 = a.rstrip('\n').split(' ')

    match = [x for x in x1 if x in y1]
    if len(match)==1:
        s.write("Case #%d: %d\n" % (i+1,int(match[0])))
    if len(match)==0:
        s.write("Case #%d: Volunteer cheated!\n" % (i+1))
    if len(match)>1:
        s.write("Case #%d: Bad magician!\n" % (i+1))
    
f.close()
s.close()
