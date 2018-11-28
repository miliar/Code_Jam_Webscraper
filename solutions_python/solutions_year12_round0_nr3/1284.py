f = open("C-small-attempt1.in", "r")
o = open("C-small-attempt1.out", "w")

def equal (m,n):
    m = str(m)
    n = str(n)
    for x in range(0,len(m)):
        if m[x:] + m[0:x] == n:
            return True
    return False

num = int(f.readline())
for s in range(0,num):
    string = f.readline().split(" ")
    a = int(string[0])
    b = int(string[1])
    count = 0
    for x in range(a,b + 1):
        for y in range(x + 1,b + 1):
            if equal(x,y) and y:
                count+= 1
    o.write("Case #" + str(s + 1) + ": " + str(count) + "\n")
            
f.close()
o.close()
