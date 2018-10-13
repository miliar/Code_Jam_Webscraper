import sys

a = open("input.in")
b = open("output.txt","w")

def magic(l):
    count = 0
    for i in l[0]:
        if i in l[1]:
            count += 1
            number = i
    if count == 1:
        return str(number)
    elif count > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"
        

for case in xrange(int(a.readline())):
    n1 = int(a.readline())
    l = []
    for i in xrange(4):
        l1 = list(map(int,a.readline().split()))
        if i == n1-1:
            l.append(l1)
    n2 = int(a.readline())
    for i in xrange(4):
        l1 = list(map(int,a.readline().split()))
        if i == n2-1:
            l.append(l1)
    line = "Case #%d: %s\n"%(case+1,magic(l))
    #print line
    b.write(line)
    
