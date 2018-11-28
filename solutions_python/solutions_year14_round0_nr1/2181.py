T = input()

TT = int(T)

for j in range(TT):
    r1 = input()
    r1 = int(r1)
    for i in range(4):
        row = input()
        if i+1 == r1:
            r1 = row
    v = r1.split(" ")
    
    
    r1 = input()
    r1 = int(r1)
    for i in range(4):
        row = input()
        if i+1 == r1:
            r1 = row
    v2 = r1.split(" ")
    v3 = (set(v) & set(v2))
    v3 = list(v3)
    if(len(v3) == 0):
        print("Case #%d: Volunteer cheated!" % (int(j)+1))
    if(len(v3) == 1):
        print("Case #%d: %d" % (j+1, int(v3[0])))
    if(len(v3) > 1):
        print("Case #%d: Bad magician!" % (j+1))
        
        