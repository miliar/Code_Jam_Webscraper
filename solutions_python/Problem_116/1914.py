f = open("A-large.in","r")
t = int (f.readline())
ent = []

def check(ent):
    for i in range(0,4):
        if ('.' not in ent[i])and ('O' not in ent[i]):
            return 0
        if ('.' not in ent[i])and ('X' not in ent[i]):
            return 1
    
    for i in range(0,4):
        a = []
        for j in range(0,4):
            a.append(ent[j][i])
        if ('.' not in a)and ('O' not in a):
            return 0
        if ('.' not in a)and ('X' not in a):
            return 1

    a = [ent[0][0],ent[1][1],ent[2][2],ent[3][3]]
    if ('.' not in a)and ('O' not in a):
        return 0
    if ('.' not in a)and ('X' not in a):
        return 1
    
    a = [ent[0][3],ent[1][2],ent[2][1],ent[3][0]]
    if ('.' not in a)and ('O' not in a):
        return 0
    if ('.' not in a)and ('X' not in a):
        return 1

    if ('.' not in ent[0]) and ('.' not in ent[1]) and ('.' not in ent[2]) and ('.' not in ent[3]):
        return 2
        
    return 3

s = open("output.out","w")
for i in range(1,t+1):
    for j in range(0,4):
        ent.append(f.readline())
    x = check(ent)
    if x == 0:
        s.write("Case #%d: X won" % i)
    if x == 1:
        s.write("Case #%d: O won" % i)
    if x == 2:
        s.write("Case #%d: Draw" % i)
    if x == 3:
        s.write("Case #%d: Game has not completed" % i)
    if i<t:
        ent.append(f.readline())
        s.write("\n")
    ent = []

f.close()
s.close()
    
