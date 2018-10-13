import sys
from pprint import pprint
lines=sys.stdin.readlines()
for i in range(0, int(lines[0])):
    n = list(set(str.split(lines[int(lines[1+i*10]) + 1 + i*10])) & set(str.split(lines[int(lines[6+i*10]) + 6 + i*10]))) 
    l = len(n)
    sys.stdout.write('Case #%d: %s\n' % (i+1, n[0] if l==1 else ("Bad magician!" if l>1 else "Volunteer cheated!"),))
