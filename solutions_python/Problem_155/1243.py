f = open("A-large.in", "r")
s = open("output.txt","w")
t = int (f.readline())
for i in range(0,t):
    x  = f.readline().split(' ')
    maxPena = int(x[0])
    parados = int(x[1][0])
    invitados = 0
    for j in range(1,maxPena + 1):
        if int(x[1][j]) > 0:
            if parados >= j:
                parados = parados + int(x[1][j])
            else:
                invitados = invitados + (j - parados)
                parados = parados + (j - parados) + int(x[1][j])
    s.write("Case #%d: %d\n" % (i+1,invitados))
f.close()
s.close()
