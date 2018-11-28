f = open("C-small-attempt3.in", 'r')
lines = int(f.readline())*2

rc = []
groups = []


def fitem(groups, rc):
    x=0
    euros = 0
    while x<int(rc[0]):
        totalpeople = 0
        y=0
        allpeople = 0
        for i in groups:
            allpeople += int(i)
        if allpeople>int(rc[1]):
            while int(rc[1])>=totalpeople+int(groups[y]):
                totalpeople += int(groups[y])
                y+=1
            euros += totalpeople
            z=0
            while z<y:
                groups.append(groups.pop(0))
                z+=1
        else:
            euros = allpeople*int(rc[0]) 
        x+=1
    return euros
    



x=0
for line in f:
    if x<lines:
        if x%2:
            groups.append(line.split())
        else:
            rc.append(line.split())
    x+=1

writer = open('output4.txt', 'w')
y=0
while y<len(groups):
    endeuro = fitem(groups[y], rc[y])
    if y<len(groups)-1:
        writer.write("Case #"+str(y+1)+": "+str(endeuro)+"\n")
    else:
        writer.write("Case #"+str(y+1)+": "+str(endeuro))
    y+=1

writer.close()
f.close()
