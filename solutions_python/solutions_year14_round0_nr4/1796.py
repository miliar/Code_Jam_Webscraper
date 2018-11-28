def choose_ken(naomi, blocks_ken):
    ken = [opt for opt in blocks_ken if opt > naomi]
    if not ken: return min(blocks_ken)
    else: return ken[0]

def war(blocks_naomi, blocks_ken):
    points = 0
    blocks_naomi.sort()
    blocks_ken.sort()
    while (blocks_naomi):
        naomi = blocks_naomi[0]
        ken = choose_ken(naomi, blocks_ken)
        if (ken < naomi):
            points = points + 1
        blocks_naomi.remove(naomi)
        blocks_ken.remove(ken)
    return points

def deceitful_war(blocks_naomi, blocks_ken):
    points = 0
    blocks_naomi.sort()
    blocks_ken.sort()
    while (blocks_naomi):
        if ([x for x in blocks_naomi if x > min(blocks_ken)]):
             told_naomi = max(blocks_ken) + 0.0000001
             ken = choose_ken (told_naomi, blocks_ken)
             naomi = min([x for x in blocks_naomi if x > ken])
        else:
            naomi = min(blocks_naomi)
            ken = choose_ken(naomi, blocks_ken)
        if (ken < naomi):
            points = points + 1
        blocks_naomi.remove(naomi)
        blocks_ken.remove(ken)
    return points


with open("D-output.txt", "w") as output:
    with open("D-small-attempt0.in", "r") as input:
        N = int(input.readline().strip())
        for i in range (0,N):
            no = int (input.readline().strip())
            
            blocks_naomi = list(map(float, input.readline().split()))
            blocks_naomi1 = blocks_naomi[:]
            blocks_ken = list(map(float, input.readline().split()))
            blocks_ken1 = blocks_ken[:]
        
            print (('Case #' + str(i+1) + ': ' + str(deceitful_war(blocks_naomi, blocks_ken)) + ' ' + str(war(blocks_naomi1, blocks_ken1))), file = output)
            




