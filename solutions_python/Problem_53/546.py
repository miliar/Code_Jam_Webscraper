f = open("A-large.in", 'r')
lines = int(f.readline())

snappers = []

x=0
for line in f:
    if x<lines:
        snappers.append(line.split())
        snappers[x][0] = int(snappers[x][0])
        snappers[x][1] = int(snappers[x][1])+1
    x+=1

f.close()
f = open("snapout.txt", 'w')

x=0
while x<len(snappers):
    if snappers[x][1]%(int("1"*snappers[x][0], 2)+1) == 0:
        f.write("Case #"+str(x+1)+": ON\n")
    else:
        f.write("Case #"+str(x+1)+": OFF\n")
    x+=1

f.close()
