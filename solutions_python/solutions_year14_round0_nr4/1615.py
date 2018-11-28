#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Andy
#
# Created:     11/04/2014
# Copyright:   (c) Andy 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def PlayWar(blocks):
    wins = 0
    global used
    used = []
    for f in range(len(N)):
        NaomiBlock = float(N[f])
        smallest = FindSmallestBlockLargerThanX(NaomiBlock)
        if smallest == 1:
            wins += 1
            used.append(FindSmallestBlockLargerThanX(0))
        else :
            used.append(smallest)
    return wins

def FindSmallestBlockLargerThanX(X):
    smallest = 1
    for f in K:
        if float(f) > X and float(f) < smallest:
            if not float(f) in used:
                smallest = float(f)
    return smallest
def FindKensSmallest():
    smallest = 1.0
    for f in range(len(K)):
        if float(K[f]) < float(smallest):
            if float(K[f]) not in used_by_Ken:
                smallest = float(K[f])
    return smallest
def SeeIfNamHasLarget(KensSmallest):
    for f in range(len(N)):
        if float(N[f]) > KensSmallest:
            if  float(N[f]) not in used_by_Nam:
                return True
    return False
def NamsLowestWinningPlay(KensSmallest):
    smallest = 1.0
    for f in range(len(N)):
        if  float(N[f]) not in used_by_Nam:
            if float(N[f]) < smallest and float(N[f]) > KensSmallest:
                smallest = float(N[f])
    return smallest
def NamsLowestLosingPlay():
    largest = 0.0
    for f in range(len(K)):
        if float(K[f]) > largest:
            if not float(K[f]) in used_by_Ken:
                largest = float(K[f])
    used_by_Ken.append(largest)
    nams_smallest = 0.0
    for f in range(len(N)):
        if float(N[f]) > nams_smallest:
            if not float(N[f]) in used_by_Nam:
                if float(N[f]) < largest:
                    nams_smallest = float(N[f])
    return nams_smallest

def PlayFakeWar():
    global used_by_Ken
    used_by_Ken = []
    global used_by_Nam
    used_by_Nam = []
    wins = 0
    for f in range(len(K)):
        KensSmallest = FindKensSmallest()
        if SeeIfNamHasLarget(KensSmallest) and KensSmallest < 1:
            wins += 1
            used_by_Nam.append(NamsLowestWinningPlay(KensSmallest))
            used_by_Ken.append(KensSmallest)
        else :
            used_by_Nam.append(NamsLowestLosingPlay())
    return wins



def main():
    input_text = open("C:\Users\Andy\Downloads\D-large.in","r")
    output_text = open("waroutput.txt","w")
    Cases = int(input_text.readline())
    game = 0
    while game < Cases:
        game += 1
        Num_of_Blocks = input_text.readline()

        N_text = input_text.readline()
        global N
        N = N_text.split()

        K_text = input_text.readline()
        global K
        K = K_text.split()

        real_war_wins = PlayWar(Num_of_Blocks)
        fake_war_wins = PlayFakeWar()
        output_text.write("Case #" + str(game) + ": " + str(fake_war_wins) + " " + str(real_war_wins))
        if not game == Cases:
            output_text.write("\n")


if __name__ == '__main__':
    main()
