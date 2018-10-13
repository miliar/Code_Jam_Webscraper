
fob = open("B-small-attempt0.in")
res = open("res.out","w")
T = int(fob.readline())


def check():
    [N,M] = fob.readline().split(' ')
    N = int(N)
    M = int(M)
    field = []
    for i in xrange(N):
        field.append(fob.readline().split())
    fields = [field, zip(*field)]
    maxrow = [max(row) for row in fields[0]]
    maxcol = [max(col) for col in fields[1]]
    for i in range(N):
        for j in range(M):
            if field[i][j] != maxrow[i] and field[i][j] != maxcol[j]:
                return "NO"
    return "YES"


    
case = 0
while case<T:
    string = "Case #"+str(case+1)+": " + check()+"\n"
    res.write(string)
    case+=1
fob.close()    
res.close()
'''
Created on 12. apr. 2013

@author: nraw
'''
