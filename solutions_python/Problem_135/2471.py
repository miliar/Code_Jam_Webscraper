f = open("A-Small.in",'r')
g = open("A-Small_Output.txt",'w')
t = int(f.readline())
for i in range(t):
    g.write("Case #"+str(i+1)+": ")
    l1= []
    l2= []
    a = int(f.readline())
    for j in range(4):
        l1.append(f.readline().strip().split())
    b = int(f.readline())
    for j in range(4):
        l2.append(f.readline().strip().split())
    c = set(l1[a-1])
    d = set(l2[b-1])
    e = c.intersection(d)
    n = len(e)
    if n == 0:
        g.write("Volunteer cheated!\n")
    elif n==1:
        q = e.pop()
        g.write(str(q)+"\n")
    else:
        g.write("Bad magician!\n")
f.close()
g.close()
    
    
