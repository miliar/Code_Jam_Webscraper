

def regwar(n, Nlist, Klist):
    score = 0
    for i in range(n):
        j = 0
        while Klist[j] < Nlist[0]:
            j += 1
            if j == n-i:
                break
        if j < n-i:
            Klist.pop(j)
        else:
            Klist.pop(0)
            score += 1
        Nlist.pop(0)
    return score

def decwar(n, Nlist, Klist):
    score = 0
    while len(Nlist) > 0 and len(Klist) > 0:
        while Nlist[0] < Klist[0]:
            Nlist.pop(0)
            if len(Nlist)==0:
                return score
        Nlist.pop(0)
        Klist.pop(0)
        score += 1
    return score

                

with open('large.in') as f:
    content = f.readlines()
content = [i.rstrip('\n').rsplit() for i in content]
for i in range(int(content.pop(0)[0])):
    n = int(content.pop(0)[0])
    Nbricks = sorted([float(j) for j in content.pop(0)])
    Kbricks = sorted([float(j) for j in content.pop(0)])
    print('Case #' + str(i+1) + ': ' + str(decwar(n,Nbricks[:],Kbricks[:])) + ' ' + str(regwar(n,Nbricks[:],Kbricks[:])))

