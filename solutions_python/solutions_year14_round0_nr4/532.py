from bisect import *

_ = int(input())
answers = []

def find_gt(a, x):
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    return False

def war(naomi, ken, n):
    #print('\n')
    #[print(end='--') for x in range(50)]
    #print('\ngiven naomi:', naomi)
    #print('given ken  :', ken, '\n')
    nscore = 0
    for i in range(n):
        f = naomi[0]
        #print('naomis:', f)
        #print('ken found:', find_gt(ken, i))
        #print(end='kens: ')
        del naomi[0]
        kens = find_gt(ken, f)
        if kens:
            ken.remove(kens)
            #print(kens)
        else:
            #print(ken[0])
            del ken[0]
            nscore += 1
    return nscore


def dwar(naomi, ken, n):
    naomi = naomi[:]
    ken = ken[:]
    nscore = 0
    for i in range(n):
        if naomi[0] < ken[0] or naomi[-1] < ken[-1]:
            del naomi[0]
            del ken[-1]
        else:
            del naomi[-1]
            del ken[-1]
            nscore+=1
    return nscore

for i in range(_):
    blocks = int(input())
    naomi = sorted(list(map(float, input().split())))
    ken = sorted(list(map(float, input().split())))

    #for j in range(blocks):
    #print(naomi)
    #print(ken)

    tap = "Case #" + str(i+1) + ":"
    answers.append(tap + ' ' +  str(dwar(naomi, ken, blocks)) + ' ' +
                                str( war(naomi, ken, blocks)))

[print(x) for x in answers]
