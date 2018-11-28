f = open("C:/Users/tadeo/Downloads/A-small-attempt0.in","r")
fw = open("C:/Users/tadeo/Downloads/A.out", "w")
n = int(f.readline())
for i in range(n):
    a1 = int(f.readline()) - 1
    c = []
    for n in range(4):
        c = c + [int(x) for x in f.readline().split(" ")]
    c1 = set(c[a1*4:a1*4+4])
    a2 = int(f.readline()) - 1

    c = []
    for n in range(4):
        c = c + [int(x) for x in f.readline().split(" ")]
    c2 = set(c[a2*4:a2*4+4])
    c = c1.intersection(c2)
    if len(c) < 1:
        s = "Volunteer cheated!"
    if len(c) == 1:
        s = str(c.pop())
    if len(c) > 1:
        s = "Bad magician!"
    fw.write("Case #"+str(1+i)+": "+s+"\n")
f.close()
fw.close()