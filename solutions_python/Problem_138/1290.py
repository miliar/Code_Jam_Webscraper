# each person gets N identical-looking blocks with mass b/w 0.0 and 1.0 exclusive

# each player knows the mass of her own blocks but not the others'

# 1. Naomi chooses a blocks
# 2. Naomi tells Ken the mass of the block
# 3. Ken chooses a block
# 4. They each put their block on one side of a scale,
#     person with heavier block gets one point.

# Both blocks are destroyed in a fire.


# Now, Naomi weighs Ken's blocks while he isn't looking
#  Naomi knows all block weights, Ken doesn't

# Naomi lies about her block weight, tells Ken, then they weigh
#  the blocks and the heavier one gets a point
# Told_naomi can't equal the mass of any of Ken's blocks

# Ken will always choose the winning block

import sys

def check_fitness(naomi, ken):
    return sum([n > k for n, k in zip(naomi, ken)])

def play_for_real(naomi, ken):
    naomi.sort(reverse=True)
    ken.sort(reverse=True)
    # naomi2 = naomi[:]
    ken2 = ken[:]

    score = 0
    # for ken_block in ken:
    #     if naomi2[0] > ken_block:
    #         score += 1
    #         naomi2 = naomi2[1:

    # if Ken knows he'll be beat, HE puts his lowest one first

    for naomi_block in naomi:
        if naomi_block > ken2[0]:
            score += 1
            # if naomi's is bigger, ken kills his lowest
            ken2 = ken2[:-1]
        else:
            # if not, ken kills his biggest
            ken2 = ken2[1:]

    return score


def play_deceptively(naomi, ken):
    naomi.sort(reverse=True)
    ken.sort(reverse=True)

    naomi2 = naomi[:]
    #ken2 = ken[:]
    score = 0

    for ken_block in ken:
        if naomi2[0] > ken_block:
            # if naomi's greatest block is bigger than ken's,
            #  naomi wins and end of story
            #ken2.remove(ken_block)
            naomi2 = naomi2[1:]
            score += 1
        else:
            # if naomi's block is smaller, ken will wins
            #  so feignt him by using naomi's smallest block
            #  but telling ken that it's just a tiny bit
            #  smaller than his largest block

            # sanity check: maybe naomi's last block is bigger
            if naomi2[-1] > ken_block:
                score += 1

            #ken2.remove(ken_block)
            naomi2 = naomi2[:-1]

    return score

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """

    for i in xrange(0, len(l), n):
        yield l[i:i+n]


inputfile = open('/home/jj/Downloads/{}'.format(sys.argv[1]), 'r')
outputfile = open('/home/jj/Desktop/out.txt', 'w')

t = inputfile.readlines()
T = int(t.pop(0))

case = 1
for triplet in chunks(t, 3):
    naomi = map(float, triplet[1].split(' '))
    ken = map(float, triplet[2].split(' '))

    deceptive= play_deceptively(naomi, ken)
    real=play_for_real(naomi, ken)

    outputfile.write("Case #{}: {} {}\n".format(case, deceptive, real))
    case += 1

inputfile.close()
outputfile.close()