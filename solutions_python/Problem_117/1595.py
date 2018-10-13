def samokec(s):
    if 2 in s:
        return False
    return True  

def presmetajs(a,b,lawn):
    lawnt = [list(tup) for tup in zip(*lawn)]
    for i in range(0,a):
        for j in range (0,b):
            if lawn[i][j] == 1 and not (samokec(lawn[i]) or samokec(lawnt[j])):
                return "NO"
    return "YES"

f = open('./input', 'rU')
f2 = open('./output', 'w')
r = ''
for i in range(int(f.readline())):
    ns = [int(x) for x in f.readline().split()]
    a = ns[0]
    b = ns[1]
    lawn = []
    for j in range(int(a)):
        lawn.append([int(x) for x in f.readline().split()])
    r+='Case #' + str(i+1) + ': ' + str(presmetajs(a,b,lawn)) + '\n'
f2.write(r)
f.close()
f2.close()
