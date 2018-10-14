def war(Naomi_w, Ken_w):
    Naomi_wins = 0
    while len(Naomi_w) > 0:
        for X in Naomi_w:
            temp = []
            done = 0
            Chosen_Naomi = X
            Told_Naomi = X
            for i in Ken_w:
                if i > X:
                    temp.append((i, i - X))
                    done = 1
            if done == 0:
                Chosen_Ken = min(Ken_w)
                Naomi_wins += 1
            else:
                Chosen_Ken = min(temp)[0]
            Naomi_w.remove(X)
            Ken_w.remove(Chosen_Ken)
    return Naomi_wins

def deceit(Naomi, Ken):
    Naomi_deceits = 0
    while len(Naomi) > 1:
        temp = []
        done = 0
##Naomi choosing and telling
        if Naomi[0] > Ken[0]:
            Chosen_Naomi = Naomi[0]
            Told_Naomi = Ken[-1]+0.0000001
        else:
            Chosen_Naomi = Naomi[0]
            Told_Naomi = Ken[-2] + (Ken[-1]-Ken[-2])/2

##Ken choosing            
        for i in Ken:
            if i > Told_Naomi:
                temp.append((i, i - Told_Naomi))
                done = 1
            if done == 0:
                Chosen_Ken = min(Ken)
            else:
                Chosen_Ken = min(temp)[0]

        if Chosen_Naomi > Chosen_Ken:
            Naomi_deceits += 1
        Naomi.remove(Chosen_Naomi)
        Ken.remove(Chosen_Ken)

##    For two blocks left
    Chosen_Naomi = Naomi[0]
    Chosen_Ken = Ken[0]
    if Chosen_Naomi > Chosen_Ken:
        Naomi_deceits += 1
    return Naomi_deceits



def deceitful_war(filename):
    file = open(filename)
    out = open("output.txt", "w+")
    testcases = int(file.readline())
    for test in range(0, testcases):
        blocks = int(file.readline())
        Naomi = file.readline().split(' ')
        Ken = file.readline().split(' ')
        Naomi_w = []
        Ken_w = []
        for i in range(0, blocks):
            Naomi[i] = float(Naomi[i])
            Ken[i] = float(Ken[i])
            Naomi_w.append(Naomi[i])
            Ken_w.append(Ken[i])
        Naomi.sort()
        Ken.sort()
        Naomi_wins = war(Naomi_w, Ken_w)
        Naomi_deceits = deceit(Naomi, Ken)

        final = ("Case #" + str(test+1) + ": " + str(Naomi_deceits) + " " + str(Naomi_wins) + "\n")
        print(final)
        out.write(final)
    file.close()
    out.close()
