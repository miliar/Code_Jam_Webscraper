#! /usr/bin/pypy

#returns weights chosen
def naomi_plays(naomi_weights):
    return naomi_weights[0]

#returns weight chosen, weight told
def naomi_cheats(naomi_weights, ken_weights):
    weight_chosen = naomi_weights[0] #choose lightest

    if weight_chosen > ken_weights[0]:
        return weight_chosen, ken_weights[-1]+1 #soo heave
    elif len(ken_weights) >= 2:
        #juust a little lighter
        weight_told = (ken_weights[-1] + ken_weights[-2]) / 2.0
        return weight_chosen, weight_told

    # tell the truth if we will win anyway
    #if ken_weights[-1] < weight_chosen:
    #    return weight_chosen, weight_chosen
    #elif len(ken_weights) >= 2:
    #    #juust a little lighter
    #    weight_told = (ken_weights[-1] + ken_weights[-2]) / 2.0
    #    return weight_chosen, weight_told
    return weight_chosen, weight_chosen

#returns weight ken plays
def ken_plays(naomi_weight_told, ken_weights):
    #find smalles weight larger than that of naomi
    #TODO: binary search would be better
    for k in ken_weights:
        if k > naomi_weight_told:
            return k

    return ken_weights[0] #smallest if nothing larger

def solve(N, weights_n, weights_k):
    weights_n.sort()
    weights_k.sort()

    war_wins = 0
    naomi_weights = weights_n[:]
    ken_weights = weights_k[:]
    for i in range(N):
        naomi_weight = naomi_plays(naomi_weights)
        ken_weight = ken_plays(naomi_weight, ken_weights)

        if ken_weight < naomi_weight:
            war_wins+=1
        naomi_weights.remove(naomi_weight)
        ken_weights.remove(ken_weight)

    deceitful_war_wins = 0
    naomi_weights = weights_n[:]
    ken_weights = weights_k[:]
    for i in range(N):
        naomi_weight_chosen, naomi_weight_told = naomi_cheats(naomi_weights, ken_weights)
        ken_weight = ken_plays(naomi_weight_told, ken_weights)

        #check stuff for dev
        if naomi_weight_chosen > ken_weight:
            if not naomi_weight_told > ken_weight:
                print "NAOMI PLAYED WRONG 1!"
                print naomi_weight_told, naomi_weight_chosen, ken_weight
                print naomi_weights
                print ken_weights
                exit(1)
        if not naomi_weight_told > ken_weight:
            if naomi_weight_chosen > ken_weight:
                print "NAOMI PLAYED WRONG 2!"
                print naomi_weight_told, naomi_weight_chosen, ken_weight
                print naomi_weights
                print ken_weights
                exit(1)
        if naomi_weight_told in ken_weights:
            print "NAOMI PLAYED WRONG 3!"
            print naomi_weight_told, naomi_weight_chosen, ken_weight
            print naomi_weights
            print ken_weights
            exit(1)

        if ken_weight < naomi_weight_chosen:
            deceitful_war_wins+=1
        naomi_weights.remove(naomi_weight_chosen)
        ken_weights.remove(ken_weight)

    return "{} {}".format(deceitful_war_wins, war_wins)

def processFile(filename):
    f = open(filename, "r")
    resultFile = open("result.txt","w")

    T = int(f.readline()) #number of cases in the first line
    print "Solving %s cases:"%(T,)

    #read the other lines
    solutions = []
    for i in range(T):
        N = int(f.readline())
        weights_n = map(float,f.readline().split(" "))
        weights_k = map(float,f.readline().split(" "))

        a = "Case #%s: %s"%(i+1, solve(N, weights_n, weights_k))
        solutions.append(a)
        print a

    resultFile.write("\n".join(map(str,solutions)))

    resultFile.close()
    f.close()

if __name__ == "__main__":
    # something which needs to be precomputed goes here

    while True:
        print "Input filename to solve:"
        fileNameToSolve = raw_input()
        processFile(fileNameToSolve)

        print "Results have been written to result.txt"
