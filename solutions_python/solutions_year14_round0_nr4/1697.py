__author__ = 'ligenjian'


def maxGreat(lista, listb):
    list1 = sorted(lista)
    list2 = sorted(listb)
    n = len(list1)
    result = []
    for i in range(n):
        result.append([0] * n)
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0:
                if list2[j] > list1[i]:
                    result[i][j] = 1
                else:
                    result[i][j] = 0
            else:
                if list2[j] > list1[i]:
                    result[i][j] = result[i-1][j-1] + 1
                else:
                    result[i][j] = max(result[i-1][j], result[i][j-1])
    return result[n-1][n-1]


inputfile = open('data/D.txt')
outputfile = open('output/D.txt','w')

t = int(inputfile.readline())

for i in range(t):
    n = int(inputfile.readline())
    print 'iter ',i
    nlist = map(float, inputfile.readline().split(' '))
    klist = map(float, inputfile.readline().split(' '))
    print>>outputfile,'Case #%d: %d %d' % (i+1, maxGreat(klist, nlist), n - maxGreat(nlist, klist))