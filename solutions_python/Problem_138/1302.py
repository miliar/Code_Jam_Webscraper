#!/usr/bin/python

def calculate_scores(blocks):
    for x in blocks:
        x.sort()
    war = play_war([x[:] for x in blocks])
    deceiptful_war = play_deceiptful_war([x[:] for x in blocks])
    return [deceiptful_war, war]
    
def play_war(sorted_blocks):
    score = 0
    for i in range(len(sorted_blocks[0])):
        naomi = optimal_war(sorted_blocks[0], None)
        ken = optimal_war(sorted_blocks[1], naomi)
        if naomi > ken:
            score += 1
    return score

def play_deceiptful_war(sorted_blocks):
    score = 0
    for i in range(len(sorted_blocks[0])):
        naomi, told = optimal_deceiptful_war(sorted_blocks[0], sorted_blocks[1], None)
        ken = optimal_war(sorted_blocks[1], told)
        if naomi > ken:
            score += 1
    return score

def optimal_war(player_sorted_blocks, current):
    if current is None:
        return player_sorted_blocks.pop(-1)
    else:
        for x in player_sorted_blocks:
            if x > current:
                player_sorted_blocks.remove(x)
                return x
        return player_sorted_blocks.pop(0)

def optimal_deceiptful_war(player_sorted_blocks, other_sorted_blocks, current):
    if current is None:
        highest_other = other_sorted_blocks[-1]
        lowest = player_sorted_blocks.pop(0)
        lowest_other = other_sorted_blocks[0]
        if lowest > lowest_other:
            tell = highest_other + 0.0000005
        else:
            tell = highest_other - 0.0000005
        return [lowest, tell]
    else:
        play = optimal_war(player_sorted_blocks, current)
        return [play, play]

def main():
    with open('input.in', 'r') as f:
        with open('output.txt', 'w') as o:
            n = int(f.readline().rstrip('\n'))
            for i in range(n):
                m = int(f.readline().rstrip('\n'))
                sorted_blocks = []
                for j in range(2):
                    sorted_blocks.append(list(map(float, f.readline().rstrip('\n').split(' '))))
                result = "Case #" + str(i + 1) + ": " + ' '.join(list(map(str, calculate_scores(sorted_blocks))))
                print(result)
                o.write(result + '\n')

if __name__=="__main__":
    main()
