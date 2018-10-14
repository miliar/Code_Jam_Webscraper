count = int(raw_input())
war = []
case = []

for i in range(count*3):
    war.append(raw_input())

for i in range(0,count*3,3):
    score = 0
    dscore = 0
    Naomi = []
    Ken = []
    dNaomi = []
    dKen = []
    N = int(war[i])
    dN = int(war[i])
    tNaomi = war[i+1].split()
    tKen = war[i+2].split()

    for t in tNaomi:
        Naomi.append(float(t))

    for t in tKen:
        Ken.append(float(t))

    Naomi.sort()
    Ken.sort()
    dNaomi = Naomi[:]
    dKen = Ken[:]
    Naomi.reverse()
    Ken.reverse()

    while N > 0:
        if Naomi[0] > Ken[0]:
            del Ken[N-1]
            score += 1
        else:
            del Ken[0]
        del Naomi[0]
        N -= 1

    while dN > 0:
        if dNaomi[0] < dKen[0]:
            del dKen[dN-1]
        else:
            del dKen[0]
            dscore += 1
        del dNaomi[0]
        dN -= 1
    case.append([dscore,score])

num = 1
for c in case:
    print 'Case #'+str(num)+': '+str(c[0])+' '+str(c[1])
    num += 1

    
