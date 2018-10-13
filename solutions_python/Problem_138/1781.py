open('output.in','w').close()

def War(naomi,ken):
    score = 0
    while len(naomi) > 0:
        win = True
        ChosenNaomi = min(naomi)
        possibilities = []
        for block in ken:
            if block > ChosenNaomi:
                win = False
                possibilities.append(block)
        if win:
            score += 1
            del ken[ken.index(min(ken))]
        else :
            ChosenKen = min(possibilities)
            del ken[ken.index(ChosenKen)]
        del naomi[naomi.index(ChosenNaomi)]
    return score
                
def DeceitfulWar(naomi,ken):
    score = 0
    while len(naomi) > 0:
        win = False
        possibilities = []
        for block in naomi:
            if block > min(ken):
                win = True
                possibilities.append(block)
        if win:
            score += 1
            ChosenNaomi = min(possibilities)
        else :
            ChosenNaomi = min(naomi)
        del naomi[naomi.index(ChosenNaomi)]
        del ken[ken.index(min(ken))]
    return score

with open('input.in') as file:
    lines = file.readlines()
    line = 0
    T = int(lines[line])
    line += 1
    for i in range(T):
        N = int(lines[line])
        line += 1
        naomi = []
        ken = []
        for n in range(N):
            naomi.append(lines[line].split()[n])
        for n in range(N):
            ken.append(lines[line+1].split()[n])
        war_points = War(naomi,ken)
        for n in range(N):
            naomi.append(lines[line].split()[n])
        for n in range(N):
            ken.append(lines[line+1].split()[n])
        dwar_points = DeceitfulWar(naomi,ken)
        with open('output.in','rw+') as file:
            file.seek(0,2)
            file.write('Case #'+str(i+1)+': '+str(dwar_points)+' '+str(war_points)+'\n')
        line += 2
