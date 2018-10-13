import sys 
lines = sys.stdin.readlines()
for i in range((int(lines[0]))):
    l = list(set(lines[10*i+1+int(lines[10*i+1])].split()) & set(lines[10*i+6+int(lines[10*i+6])].split()))
    if len(l) == 1: print "Case #"+str(i+1)+":", l[0]
    if len(l) > 1: print "Case #"+str(i+1)+":", "Bad magician!"
    if len(l) == 0: print "Case #"+str(i+1)+":", "Volunteer cheated!"
