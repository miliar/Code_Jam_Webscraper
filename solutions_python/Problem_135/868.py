f = open("A-small-attempt0.in","r")
f2 = open("output.txt","w")
t = f.readline()
for j in range(int(t)):
    k = f.readline()
    for i in range(4):
        if i+1 == int(k):
            ar = map(int,f.readline().split())
        else:
            f.readline()
    k = f.readline()
    for i in range(4):
        if i+1 == int(k):
            ar1 = map(int,f.readline().split())
        else:
            f.readline()
    br = [0 for i in range(17)]
    c = 0
    for i in ar:
        br[i] +=1
    for i in ar1:
        br[i] +=1
    for i in range(17):
        if br[i] > 1:
            c +=1
            temp = i
    if c == 1:
        f2.write("Case #%d: " %(j+1))
        f2.write("%d" %temp)
    elif c > 1:
        f2.write("Case #%d: Bad magician!" %(j+1))
    else:
        f2.write("Case #%d: Volunteer cheated!" %(j+1))
    f2.write("\n")
    
    