import re

f = open("in", 'r')

ldn = f.readline()

l = int(ldn.split()[0])
d = int(ldn.split()[1])
n = int(ldn.split()[2])


words = []

for x in range(0, d):
    line = f.readline()
    words.append(line.strip())
    
for x in range(0, n):
    r = f.readline().strip()
    r = r.replace('(', '[')
    r = r.replace(')', ']')
    prog = re.compile(r)
    cnt = 0
    for w in words:
        if prog.match(w): 
            cnt = cnt+1

    print "Case #%d: %d" % (x+1, cnt)
    
