

def getAllPermutations(x, A, B):
    results = []
    xi = x
    x = str(x)
    for i in range(len(x), 0,-1):
        tmp = x[i:] + x[0:i]
        if (tmp != x and int(tmp[0]) != 0):
            tmpint = int(tmp)
            if (tmpint >= A and tmpint <= B):
                tmin = min(xi,tmpint)
                tmax = max(xi,tmpint)
                results.append((tmin, tmax))
                
#                results.append(tmpint)
    return results

def isGood(x, A, B):
    return (len(getAllPermutations(x, A, B)) > 0)

def getAll(A, B):
    table = []
    for i in range(1+B-A):
        table.append(False)
        
    res = []
    for x in range(A, B+1):
        perm = getAllPermutations(x,A,B)
        if len(perm) != 0:
            res.extend(perm)
#        if isGood(x, A, B):
 #           res.append(x)
    return res


def rlygetAll(A,B):
     return set(getAll(A, B))
def getRes(A,B):
    return len(rlygetAll(A,B))


def main():
    lines = []
    f = open('data.txt',"r")
    for i in f:
        lines.append(i)
    n = int(lines[0])
    for ln in range(1,len(lines)):
        t = lines[ln].split(" ")
        A = int(t[0])
        B = int(t[1])
        res = getRes(A, B)
        print("Case #" + str(ln) + ": " + str(res))



if __name__ == "__main__":
    main()
