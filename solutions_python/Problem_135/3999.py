def intersect(a, b):
    return list(set(a) & set(b))
 
numOfEx = int(raw_input())
print numOfEx
for i in xrange(numOfEx):
    fc = int(raw_input())
    table1 = []
    for k in xrange(4):
        table1.append(raw_input().split())
    fl = table1[fc-1]
   
    sc = int(raw_input())
   
    table2 = []
    for j in xrange(4):
        table2.append(raw_input().split())
    sl = table2[sc-1]
    res = intersect(fl, sl)
    if len(res) == 1:
        print "Case #"+str((i+1))+":",res[0]
    elif len(res) > 1:
        print "Case #"+str((i+1))+":","Bad magician!"
    elif len(res) == 0:
        print "Case #"+str((i+1))+":","Volunteer cheated!"