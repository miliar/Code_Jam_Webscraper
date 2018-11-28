f_in = open("D-large.in", 'r')
f_out = open("d_real_large.out", 'w')

def get_int():
    return int(f_in.readline().rstrip())

def get_blocks():
    line = f_in.readline().rstrip()
    split = line.split()
    return [float(i) for i in split]

def ken_move(played, ken):
    # If he can beat it, he plays smallest larger block
    ken_sorted = sorted(ken)
    for block in ken_sorted:
        if block > played:
            return block
    # otherwise play smallest block
    return ken_sorted[0]

def war(naomi, ken):
    score = 0
    for block in naomi:
        kenblock = ken_move(block, ken)
        ken.remove(kenblock)
        if block > kenblock:
            score += 1
    return score

def dwar(naomi, ken):
    n = sorted(naomi)
    k = sorted(ken)
    #print n
    #print k
    score = 0
    # chosenN > chosenK iff toldN > chosenK
        # ie can only win a round if told is larger than all of ken's
    # toldN != any of K
    # naomi says something larger than all of his -> he plays his smallest
    # naomi says something in between two of his -> he will play larger
        # (but she can play smaller than what he says)

    # Naomi strategy: claim slightly below ken's largest to force him to play it -> play naomi's smallest
    # until she can beat him?

        # Naomi claims something higher than all of Ken's, he plays his lowest, so does Naomi, naomi wins

    # While k has blocks larger than n's largest, n plays lowest and claims in between k's highest and 2nd highest

    while len(n) > 1:
        
        # Naomi's smallest cannot beat his smallest: throw it away with ken's highest
        if n[0] < k[0]:
            
            #print n[0], k[-1]
            n.remove(n[0])
            k.remove(k[-1])
        # Naomi can win by cheating: her smallest can beat ken's smallest
        elif n[0] > k[0]:
            # Claim larger than all of kens
            #print n[0], k[0]
            n.remove(n[0])
            k.remove(k[0])
            score += 1
        # Naomi can win this round (her largest can beat ken's largest)
        elif n[-1] > k[-1]:

            
            #print n[-1], k[0]
            n.remove(n[-1])
            k.remove(k[0])
            score += 1

         # Naomi's largest cannot beat Ken's largest
        elif n[-1] < k[-1]:
            #print n[0], k[-1]
            # Claim in between Ken's largest and 2nd largest, and play lowest (ken plays highest)
            n.remove(n[0])
            k.remove(k[-1])




    # Last round: both have to play without deceit
    if n[0] > k[0]:
        score += 1
        #print n[0], k[0]
    return score

T = get_int()

for case in range(1, T + 1):
    blocks = get_int()
    naomi = get_blocks()
    ken = get_blocks()

    f_out.write("Case #{0}: {1} {2}\n".format(case, dwar(naomi, ken), war(naomi, ken)))

f_in.close()
f_out.close()
