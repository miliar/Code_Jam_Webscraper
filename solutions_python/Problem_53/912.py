def snap(l):
    a = []
    for i, s in enumerate(l):
        a.append(not s)
        if s == False:
            a.extend(l[i+1:])
            break
    return a
def is_on(l):
    if False in l:
        return False
    return True
file = open("A-small-attempt0.in","r")
out = open("Out2.out","w")
s = int(file.readline().rstrip())
for i in range(1,s+1):
    t = map(int,file.readline().rstrip().split())
    q = [False for e in range(t[0])]
    for z in range(t[1]):
        q = snap(q)
    out.write("Case #%d: %s\n" % (i, "ON" if is_on(q) else "OFF"))
