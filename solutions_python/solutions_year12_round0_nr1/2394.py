import sys


case = 1

lines = sys.stdin.readlines()
count = (len(lines)-1)/2

map = dict()


for i in range(count):
    line1 = lines[i+1]
    line2 = lines[i+count+1]
    #print line1, line2

    for j in range(len(line1)):
        map[line1[j]] = line2[j]

map['q'] = 'z'
map['z'] = 'q'

f = open('A-small-attempt0.in', 'r')

case = 1
for line in f.readlines()[1:]:
    res = ""
    for char in line.strip():
        res += map[char]

    print "Case #%d: %s" % (case, res)
    case += 1
