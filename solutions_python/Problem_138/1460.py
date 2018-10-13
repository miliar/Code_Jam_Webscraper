__author__ = 'kurtis'

def isGreaterListCompare(lessThanList, moreThanList):
    for i in xrange(len(lessThanList)):
        if lessThanList[i] >= moreThanList[i]:
            return False
    return True

def calculate_case(case_number, finput):
    number_of_blocks_per_player = int(finput.readline())
    blocks_given_naomi = map(float, finput.readline().split(" "))
    blocks_given_naomi.sort()
    blocks_given_ken = map(float, finput.readline().split(" "))
    blocks_given_ken.sort()
    points_war_naomi = 0
    points_deceitful_war_naomi = 0

    blocks_war_naomi = list(blocks_given_naomi)
    blocks_war_ken = list(blocks_given_ken)
    # Strategy for War
    for round in xrange(number_of_blocks_per_player):
        block_from_naomi = blocks_war_naomi.pop(0)
        # Get a list of all of Ken's blocks that are higher than Naomi's
        higher_blocks_from_ken = ([i for i in blocks_war_ken if i > block_from_naomi])
        if len(higher_blocks_from_ken) > 0:
            # Ken won this round
            higher_blocks_from_ken.sort(reverse=True)
            blocks_war_ken.remove(higher_blocks_from_ken.pop())
        else:
            # Naomi won this round
            # Get rid of Ken's lowest block
            blocks_war_ken.pop(0)
            points_war_naomi += 1

    blocks_deceitful_war_naomi = blocks_given_naomi
    blocks_deceitful_war_ken = blocks_given_ken
    # Strategy for Deceitful War
    for round in xrange(number_of_blocks_per_player):
        # Determine if every matching value of Naomi's is larger than Ken's
        # If so, Noami can easily win
        # Otherwise, she just kills off Ken's highestblocks, which is below
        if isGreaterListCompare(blocks_deceitful_war_ken, blocks_deceitful_war_naomi):
            # Okay this game is over!
            points_deceitful_war_naomi += len(blocks_deceitful_war_naomi)
            break

        # Okay, we need to play the killoff strategy against Ken's blocks to begin the game
        # Naomi plays her lowest blocks, while telling Ken she is playing high blocks
        # Ken feels forced to play his highest block for this round
        blocks_deceitful_war_naomi.pop(0)
        blocks_deceitful_war_ken.pop()



    message = "Case #" + str(case_number) + ": " + str(points_deceitful_war_naomi) + " " + str(points_war_naomi)
    return message

def print_message(message, foutput):
    print message
    foutput.write(message + "\n")

if __name__ == "__main__":
    fin = open('D-large.in', 'r')
    fout = open('problemd.out','w')
    number_of_cases = int(fin.readline())
    for i in xrange(number_of_cases):
        message = calculate_case(i+1, fin)
        print_message(message, fout)
    fin.close()
    fout.close()