import copy

def min_than_value(array, min_value):
    for i in array:
        if i > min_value:
            return i
    return array[-1]

def max_under_value(array, max_value):
    for i in reversed(array):
        if i < max_value:
            return i
    return array[-1]

def who_wins(naomi_block, ken_block):
    if naomi_block > ken_block:
        return 1
    else:
        return 0

fInput = open("input4.txt", "r")
fOutput = open("output4.txt", "w")

number_of_cases = int(fInput.readline())
for number_case in range(1, number_of_cases+1):
    number_of_blocks = int(fInput.readline())
    naomi_blocks = [float(x) for x in fInput.readline().split(" ")]
    naomi_blocks.sort()
    ken_blocks = [float(x) for x in fInput.readline().split(" ")]
    ken_blocks.sort()
    score_war = 0
    score_dwar = 0
    naomi_hand_war = copy.copy(naomi_blocks)
    naomi_hand_dwar = copy.copy(naomi_blocks)
    ken_hand_war = copy.copy(ken_blocks)
    ken_hand_dwar = copy.copy(ken_blocks)
    for i in range(0, number_of_blocks):
        # On prend le plus petit bloc de chez Naomi si ils jouent à War
        naomi_smaller_block = min(naomi_hand_war)
        naomi_hand_war.remove(naomi_smaller_block)
        # On prend le plus petit bloc de chez Ken si ils jouent à War
        ken_block_war = min_than_value(ken_hand_war, naomi_smaller_block)
        ken_hand_war.remove(ken_block_war)
        score_war += who_wins(naomi_smaller_block, ken_block_war)
        # Si ils jouent à dWar, on prend le plus gros bloc de Naomi
        naomi_higher_block = max(naomi_hand_dwar)
        naomi_hand_dwar.remove(naomi_higher_block)
        # On prend pour Ken le bloc "juste" en dessous de celui de Naomi
        ken_block_dwar = max_under_value(ken_hand_dwar, naomi_higher_block)
        ken_hand_dwar.remove(ken_block_dwar)
        score_dwar += who_wins(naomi_higher_block, ken_block_dwar)
    fOutput.write("Case #" + str(number_case) + ": " + str(score_dwar) + " " + str(score_war) + "\n")
    print(str((number_case/number_of_cases)*100) + "%")

fInput.close()
fOutput.close()