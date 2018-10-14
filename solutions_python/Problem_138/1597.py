

def play_war(p1, p2):
    p2 = sorted(p2) # smallest to largest, in place

    for chosen_p1 in p1:
    # each Naomi turn
    
        for option_p2 in p2:
            p2_won = 0
            if option_p2 > chosen_p1:
                p2.remove(option_p2)
                break

    p1_score = len(p2) # this is too clever, but correct
    return p1_score

def play_deceitful_war(p1, p2):
    p1.sort()
    p2.sort()
    p1_score = 0
    #print p1
    #print p2

    for i in range(len(p1)):
        if p1[-1] > p2[-1]:
            p1_score += 1
            del p1[-1]
            del p2[-1]
        else:
            del p1[0]
            del p2[-1]

    return p1_score



f = open('D-large.in', 'r')
results = open('war.out', 'w')

T = f.readline()

for i in range(int(T)):
    N = f.readline() # number of blocks per player
    naomi = [float(s) for s in f.readline().split()] # naomi's block weights
    ken = [float(s) for s in f.readline().split()] # ken's block weights

    war_result = play_war(naomi, ken)
    deceit_result = play_deceitful_war(naomi, ken)

    #print i+1, deceit_result, war_result
    results.write("Case #{}: {} {}\n".format(i+1, deceit_result, war_result))
    

f.close()
results.close()
print "done"
