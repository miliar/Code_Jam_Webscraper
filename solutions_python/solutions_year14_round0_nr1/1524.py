f = open('A-small-attempt1.in', 'r')
w = open('OUT1.txt','w')
n = int(f.readline())

for q in range (n):
    a = int(f.readline())
    x = []
    c = 0
    k = ''
    for i in range (4):
        t = f.readline()
        if i == (a - 1):
            x = t.strip().split()
    b = int(f.readline())
    y = []
    for i in range (4):
        t = f.readline()
        if i == (b - 1):
            y = t.strip().split()
    for i in x:
        for j in y:
            if i == j:
                c += 1
                k = i
    if c > 1:
        w.writelines ('Case #' + str(q+1) + ": Bad magician!\n")
    elif c == 1:
        w.writelines ('Case #' + str(q+1) + ": " + k + "\n")
    else:
        w.writelines ('Case #' + str(q+1) + ": Volunteer cheated!\n")

f.close()
w.close()