fin = open('D-large.in','r')

cases = int(fin.readline().strip())

a = 1

def war(naomi, ken):
    naomi = naomi[:]
    ken = ken[:]
    point = 0
    while len(naomi) and len(ken):
        if float(naomi[0]) > float(ken[0]):
            point += 1
            naomi.pop(0)
            ken.pop(len(ken)-1)
        else:
            naomi.pop(0)
            ken.pop(0)
    return point
 
def deceitful(naomi, ken):
    naomi = naomi[:]
    ken = ken[:]
    point = 0
    while len(naomi) and len(ken):
        if float(naomi[len(naomi)-1]) < float(ken[len(ken)-1]):
            naomi.pop(len(naomi)-1)
            ken.pop(0)
        else:
            naomi.pop(len(naomi)-1)
            ken.pop(len(ken)-1)
            point += 1
    return point

while a <= cases:
    numBlocks = int(fin.readline().strip())
    naomiBlocks = fin.readline().strip().split(' ')
    naomiBlocks.sort(reverse=True)
    kenBlocks = fin.readline().strip().split(' ')
    kenBlocks.sort(reverse=True)
    warPoints = war(naomiBlocks, kenBlocks)
    deceitfulPoints = deceitful(naomiBlocks, kenBlocks)        
    print('Case #' + str(a) + ': ' + str(deceitfulPoints) + ' ' + str(warPoints))

    a+=1
