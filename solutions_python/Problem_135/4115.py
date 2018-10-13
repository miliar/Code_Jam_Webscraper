import sys

def parse_block():
    n = int(input())
    table = []
    for raw in range(4):
        table.append([]);
        for item in input().split(' '):
            table[raw].append(int(item))
    return set(table[n-1])


f = open('workfile', 'w')
T = int(input())
for testN in range(T):
    raw1 = parse_block()
    raw2 = parse_block()
    both = set.intersection(raw1, raw2)
    f.write("Case #" + str(testN+1) + ": ")
    if (len(both) < 1):
        f.write("Volunteer cheated!\n")
    elif (len(both) > 1):
        f.write("Bad magician!\n")
    else:
        f.write(""+str(list(both)[0])+"\n")



