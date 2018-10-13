import functools
import time


inputStr = '''5
2 1
ik
3 1
ijk
3 1
kji
2 6
ji
1 10000
i'''
mo = -1
o = 1
i = 'i'
j = 'j'
k = 'k'



itt = iter(inputStr.split('\n')[1:])
pairInput = zip(itt, itt)

matrix = {o:{o:[o], i:[i], j:[j], k:[k]},
          i:{o:[i], i:[mo], j:[k], k:[mo, j]},
          j:{o:[j], i:[mo, k], j:[mo], k:[i]},
          k:{o:[k], i:[j], j:[mo, i], k:[mo]}}

def getResFor(a,b):
    return matrix[a][b]

def removeDoubleNegatives(strA):
    if strA.count(mo) > 0:
        if strA.count(mo) % 2 == 0:
            return list(filter(lambda x: x != mo, strA))
        else:
            aa = list(filter(lambda x: x != mo, strA))
            aa.append(mo)
            return aa
    return strA


for ind, case in enumerate(pairInput):

    toGet = [i, j, k]


    mult = int(case[0].split(' ')[1])
    caseStr = case[1] * mult
    strA = list(caseStr)

    while len(strA) > 1:

        if len(strA) < len(toGet):
            break

        if strA == toGet:
            strA = []
            toGet = []
            break

        if toGet and strA[0] == toGet[0]:
            strA.pop(0)
            toGet.pop(0)

        if len(strA) == 2 and -1 in strA:
            break

        if strA[0] == -1 or strA[1] == -1:
            strA = removeDoubleNegatives(strA)
            break


        a = strA.pop(0)
        b = strA.pop(0)


        res = getResFor(a, b)
        if not toGet or res != toGet[0]:
            if len(res) == 2:
                strA.append(-1)
                strA.insert(0, res[1])
            elif res[0] == -1:
                strA.append(-1)
            else:
                strA.insert(0, res[0])

            if a == -1 or b == -1:
                strA = removeDoubleNegatives(strA)
        else:
            toGet.pop(0)



    if not toGet and not strA:
        print('Case #{0}: YES'.format(ind+1))
    else:
        print('Case #{0}: NO'.format(ind+1))


