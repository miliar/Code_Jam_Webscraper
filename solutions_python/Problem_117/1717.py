#!python3

#wow...
f = open("B-small-attempt3.in", 'r')
g = open("out-B-small.txt", 'w')

stuff = f.read()
f.close()

L = stuff.split("\n")
cases = int(L.pop(0))

def changes(row):
    if 1 in row:
        if 2 in row:
            return False
        else:
            return True
    else:
        return True

def oneortwo(x):
    pie = []
    for i in x:
        if i:
            pie.append(1)
        else:
            pie.append(2)
    return pie

def check(rows, cols):
    rowr = []
    colr = []
    result = []
    for row in rows:
        rowr.append(changes(row))
    for col in cols:
        colr.append(changes(col))

    #print(rowr, colr)
    for i in rowr:
        result.append([])
        for j in colr:
            result[-1].append(i or j)
            
    result = list(map(oneortwo, result))
    print(result)
    return result == rows

for case in range(cases):
    dim = L.pop(0).split(" ")
    dim = [int(x) for x in dim]
    if min(dim) == 1:
        for i in range(dim[0]):
            L.pop(0)
        g.write("Case #{}: YES\n".format(case+1))
        continue
    
    length = dim[0]
    rows = []
    for i in range(length):
        pie = L.pop(0).split(" ")
        pie = [int(x) for x in pie]
        rows.append(pie)

    cols = list(zip(*rows))

    works = check(rows, cols)

    if works:
        answer = "YES"
    else:
        answer = "NO"

    g.write("Case #{}: {}\n".format(case+1, answer))
g.close()
