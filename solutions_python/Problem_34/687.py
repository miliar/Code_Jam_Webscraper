#": Ben Steenhuisen
from re import *
fin = file("A-large.in","r")
fout = file("out.txt","w")
line1 = fin.readline()
l,d,n = int(line1.split()[0]),int(line1.split()[1]),int(line1.split()[2])
#print l,d,n
ls = []
for x in xrange(d):
    ls.append(fin.readline().strip())

#print ls

for x in xrange(n):
    overall = "^"
    cur = fin.readline().strip()
    inside = 0
    for char in cur:
        if (char=="("):
            inside+=1
        elif (char==")"):
            overall = overall[:-1]
            inside-=1
        overall+=char
        if inside: overall+="|"
    overall += "$"
    overall = overall.replace("(|","(").replace(")|",")")
    #print overall
    matches = 0
    for y in ls:
        if search(overall,y):
            matches+=1
    fout.write("Case #"+str(x+1)+": "+str(matches)+"\n")

fout.close()
