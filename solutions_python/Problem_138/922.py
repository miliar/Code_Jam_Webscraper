import fileinput
from bisect import bisect_left

def main():
    # read all input data into a list and reverse it to make it easy
    # to pop off.
    input_data = []
    for line in fileinput.input():
        input_data.append(line.strip())
    input_data = input_data[::-1] # reverse list

    # number of games
    num_games = int(input_data.pop())

    for i in range(num_games):
        num_blocks_each = input_data.pop()
        naomi_blocks = [float(b) for b in input_data.pop().split(' ')]
        ken_blocks = [float(b) for b in input_data.pop().split(' ')]
        # note we use [:] notation to copy list so that side effects
        # don't occur if the optimizing functions decide to mutate the
        # arguments.
        naomi_war_score = optimize_war(naomi_blocks[:],
                                        ken_blocks[:])
        naomi_deceit_score = optimize_deceitful_war(naomi_blocks[:],
                                        ken_blocks[:])
        print ''.join(['Case #', str(i + 1), ': ',
                       str(naomi_deceit_score), ' ', str(naomi_war_score)])
        

def optimize_war(naomi, ken):
    """ Optimize Naomi's strategy for a regular game of war.

    Parameters:

    naomi -- a list of Naomi's block sizes (float numbers)
    ken -- a list of Ken's block sizes (float numbers)

    Returns an integer describing the maximum score Naomi can achieve
    playing war optimally.

    """
    
    naomi.sort() # sort smallest to largest
    ken.sort() # sort smallest to largest
    naomi_score, ken_score = 0, 0
    while len(naomi) > 0:
        # Naomi chooses largest
        naomi_choice = naomi.pop()
        # Ken looks for smallest item larger than Naomi's
        ind = bisect_left(ken, naomi_choice)
        if ind == len(ken):
            # Ken has nothing that beats Naomi's, so sacrifice Ken's smallest
            ken_choice = ken[0]
            naomi_score += 1
        else:
            # Ken uses his smallest block larger than Naomi's chosen
            # block
            ken_choice = ken[ind]
            ken_score += 1
        # burn Ken's chosen block
        ken.remove(ken_choice)
    return naomi_score

def optimize_deceitful_war(naomi, ken):
    """ Optimize Naomi's strategy for deceitful war.

    Parameters: same as optimize_war()

    Returns an integer describing the maximum score Naomi can achieve
    playing deceitful war optimally.

    """
    #print 'naomi in:', str(naomi)
    #print 'ken in:', str(ken)
    naomi.sort() # sort smallest to largest
    ken.sort() # sort smallest to largest
    naomi_score, ken_score = 0, 0

    #print 'naomi sorted:', naomi
    #print 'ken sorted:', ken

    while len(naomi) > 0:
        # Naomi works from her smallest blocks to her highest.  If her
        # smallest block is smaller than Ken's, then she at least
        # phonies up the number to Ken's biggest - epsilon to make Ken
        # dispose of his best.  If her smallest is bigger than Ken's
        # smallest, she phonies up the number to be greater than Ken's
        # greatest.  Because Ken chooses his smallest when he thinks
        # he's about to lose, Naomi's smallest still shows up bigger
        # on the scale.
        naomi_choice = naomi[0]
        if naomi[0] < ken[0]:
            # Naomi has to lose, but might as well make Ken burn his
            # biggest
            ken.pop() # remove biggest
            ken_score += 1
        else:
            # Naomi phonies up the number to be bigger than Ken's
            # biggest.  Ken aquiesces by giving up his smallest, which
            # is smaller than what Naomi will put on the scales
            # anyway.
            ken_choice = ken[0]
            ken.remove(ken_choice)
            naomi_score += 1
        naomi.remove(naomi_choice)
    
    # another broken strat
    # while len(naomi) > 0:
    #     # Naomi seeks to diminish as many of Ken's high ranking blocks
    #     # as possible with dummy size quotes.  Only when all of her
    #     # blocks are heavier than Ken's heaviest does she put forward
    #     # her real blocks with real quotes
    #     if naomi[0] < ken[-1]:
    #         # Naomi's smallest is smaller than Ken's biggest.
    #         # She dummies the quote to be infinitesimally smaller than
    #         # Ken's largest and then burns her smallest block on the
    #         # scale while Ken burns his largest.
    #         ken_choice = ken.pop()
    #         naomi_choice = naomi[0]
    #         naomi.remove(naomi_choice)
    #         ken_score += 1
    #     else:
    #         # Naomi's smallest block is now larger than Ken's
    #         # remaining largest.  She can now win every remaining
    #         # round.
    #         naomi_choice = naomi.pop()
    #         ken_choice = ken[0]
    #         ken.remove(ken_choice)
    #         naomi_score += 1
    #     print 'naomi choice:', str(naomi_choice)
    #     print 'ken choice:', str(ken_choice)
    
    # old broken strategy
    # while len(naomi) > 0:
    #     # In each round if Naomi's largest block is bigger than Ken's
    #     # largest, she offers her largest at true weight and wins the
    #     # point.  If Naomi's largest block is smaller than Ken's
    #     # largest, she phonies up the number to be infinitesimally
    #     # smaller than Ken's largest to force Ken to give up his
    #     # largest block.  She then offers her smallest block on the
    #     # scales.
    #     if naomi[-1] > ken[-1]:
    #         # Naomi can win this round.
    #         naomi_choice = naomi.pop()
    #         ken_choice = ken[0]
    #         ken.remove(ken_choice)
    #         naomi_score += 1
    #     else:
    #         # Naomi can't win this round, but can force Ken to give up
    #         # his greatest block while given up her smallest block.
    #         naomi_choice = naomi[0]
    #         naomi.remove(naomi_choice)
    #         ken.pop()
    #         ken_score += 1
    
    return naomi_score

if __name__ == '__main__':
    main()
