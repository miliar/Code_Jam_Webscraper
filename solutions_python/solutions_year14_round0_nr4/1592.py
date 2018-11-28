def get_optimal(num, pieces):
    #get the smallest number that can beat this, otherwise return the lowest item in the list
    if max(pieces) > num:
        #find the smallest piece that's larger than num
        smallest_large = 0.0
        for i in pieces:
            if(i > num):
                smallest_large = i
            else:
                break
        return smallest_large
    else:
        # return the minimum in the list
        return min(pieces)


def naomi_wins_regular_war(n, k):
    n = sorted(n, key=float, reverse = True)
    k = sorted(k, key=float, reverse = True)
    naomi_wins = 0
    for i in n:
        optimal = get_optimal(i, k)
        if i > optimal:
        #    print "Ken: ", optimal
        #    print "Nao: ", i, " win"
            naomi_wins += 1
        #else:
        #    print "Ken: ", optimal, ""
        #    print "Nao: ", i

        # remove optimal from ken's list
        k.remove(optimal)
    return naomi_wins


def naomi_wins_deceitful_war(n, k, N):

    naomi_wins = 0
    for i in range(N):

        #n = sorted(n, key=float, reverse = False)
        #k = sorted(k, key=float, reverse = False)

        #print n
        #print k

        #if naomi has the smallest card of her and ken, she must lie to get rid of the largest card
        if min(n) < min(k):
            #print "Ken: ", max(k), " win"
            #print "Nao: ", min(n), ""
            k.remove(max(k))
            n.remove(min(n))
            continue

        #lie to ken and say you have a very large log forcing him to select his smallest
        if min(n) > min(k):
            #print "Ken: ", min(k), ""
            #print "Nao: ", min(n), " win"
            k.remove(min(k))
            n.remove(min(n))
            naomi_wins += 1
            continue



    return naomi_wins



#filename = "D-small-attempt0.in"
filename = "D-large.in"

fin  = open(filename,'r')
fout = open("output_" + filename,'w')

cases = int(fin.readline())

for c in range(cases):
    N     = int(fin.readline())
    naomi = [float(x) for x in fin.readline().strip().split(' ')]
    ken   = [float(x) for x in fin.readline().strip().split(' ')]

    reg = naomi_wins_regular_war(naomi, ken)
    dec = naomi_wins_deceitful_war(naomi, ken, N)

    #print "Case #" + str(c + 1) + ": " + str(dec), str(reg)
    fout.write("Case #" + str(c + 1) + ": " + str(dec) + " " + str(reg) + "\n")
