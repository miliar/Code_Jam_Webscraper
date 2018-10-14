
__author__ = 'sergeyy'
import time


def War(naomi, ken, nim):
    naomi = sorted(naomi, reverse=True)
    ken = sorted(ken, reverse=True)
    score = 0
    while naomi:
        n = naomi.pop()
        if max(ken)<n:
            ken.pop()
            score += 1
        else:
            for k in ken[::-1]:
                if k>n:
                    ken.remove(k)
                    break

    return str(score)


#def DWar(naomi, ken, num):
#    k = min(ken)
#    naomi = sorted(naomi)
#    score = len(naomi)
#    for n in naomi:
#        if n<k:
#            score-=1
#    return str(score)

def DWar(naomi, ken, num):
    ken = sorted(ken)
    score = 0
    naomi = sorted(naomi)
    while naomi:
        k = min(ken)
        if max(naomi)<k:
            break
        for n in naomi:
            if n>k:
                score+=1
                ken.remove(k)
                naomi.remove(n)
                break



    return str(score)

def check(naomi, ken, n):
    return DWar(naomi, ken, n) + ' ' + War(naomi, ken, n)

case = 1
with open('input.txt', 'r') as fin:
    with open('output.txt', 'w') as fout:
        cnt = int(fin.readline())
        for i in range(1, cnt+1):
            n = int(fin.readline())
            naomiStr = fin.readline()
            naomi = []
            for s in naomiStr[:-1:].split(' '):
                naomi.append(float(s))

            kenStr = fin.readline()
            ken = []
            for s in kenStr[:-1:].split(' '):
                ken.append(float(s))

            oline = ''
            oline = 'Case #' + str(i) +': ' + check(naomi, ken, n) +'\n'
            fout.write(oline)

#print (time.clock())



