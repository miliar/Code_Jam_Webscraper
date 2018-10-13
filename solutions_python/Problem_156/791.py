import sys
import math
from bisect import bisect_left, bisect_right

if len(sys.argv) > 1:
    inf = open(sys.argv[1])
else:
    inf = open('b.in')


T = int(inf.readline())

def trim(lista):
    """
    >>> trim([0, 0, 0, 1, 2, 3])
    [1, 2, 3]
    >>> trim([0, 0])
    []
    """
    if lista[0] != 0:
        return lista
    if lista[-1] == 0:
        return []

    i = bisect_right(lista, 0)
    return lista[i:]




global seen 

def bruteforce(lista, mins, max):
    lista = tuple(lista)    
    global seen

    if mins > max:
        return max

    if lista in seen:
        return seen[lista]

    # print lista
    if len(lista) == 0:
        return mins
    if lista[-1] <= 1:
        return mins + 1

    M = lista[-1]
    mitad = int(math.ceil(M/2.))

    # dividir
    t1 = []
    for i in range(1, mitad + 1):
        l1 = list(lista[:-1]) + [M - i, i]
        l1.sort()


        t1.append(bruteforce(l1, mins + 1, max))

    # comer
    t1 = min(t1)
    t2 = bruteforce([x-1 for x in lista], mins + 1, max)

    seen[lista] = min(t1, t2)

    return min(t1, t2)


for x in range(1,T+1):
    D = int(inf.readline())
    diners = map(int, inf.readline().split(' '))
    diners.sort()

    mins = 0

    # while len(diners)>0:
    #     # print diners
    #     M = diners[-1]
    #     mitad = int(math.ceil(M/2.))
        
    #     n = len(diners) - bisect_right(diners, mitad)
    #     #print mitad, n

    #     if M - mitad > n:
    #         # divido

    #         diners.pop()
    #         diners.insert(bisect_left(diners, mitad), mitad)
    #         diners.insert(bisect_left(diners, M - mitad), M - mitad)
    #         # print 'dividiendo'

    #     else:
    #         # espero
    #         diners = [i-1 for i in diners]
    #         # print 'esperando'

    #     diners = trim(diners)


    #     mins += 1

    global seen
    seen = dict()
    mins = bruteforce(diners, 0, diners[-1])


    print 'Case #%d: %d' % (x, mins)