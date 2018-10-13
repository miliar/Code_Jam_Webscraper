import random

def solve(conn):
    count = 0
    for (al,ar) in conn:
        for (bl,br) in conn:
            if al < bl and ar > br:
                count += 1
    return count


input = open("A-large.in")
output = open("A-large.out","w")

"""
for n in range(int(input.readline())):
    conn = []
    for k in range(1000):
        conn.append([random.randint(1,10**4),random.randint(1,10**4)])    
    output.write("Case #%s: %s\n" % (n+1,solve(conn)))

"""
for n in range(int(input.readline())):
    print n
    conn = []
    for k in range(int(input.readline())):
        conn.append([int(v) for v in input.readline().split(" ")])
    
    output.write("Case #%s: %s\n" % (n+1,solve(conn)))

input.close()