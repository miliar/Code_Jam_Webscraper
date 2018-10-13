__author__ = 'sean223'


# IN_FILE = 'test_input.txt'
# OUT_FILE = 'test_output.txt'

IN_FILE = 'C-small.in'
OUT_FILE = 'small_out.txt'

# IN_FILE = 'C-large.in'
# OUT_FILE = 'large_out.txt'


with open(IN_FILE, 'r') as fileIn:
    fileLines = fileIn.readlines()

it = iter(fileLines)
numbCases = int(next(it))
output = ""


for case in range(1, numbCases+1):
    hd, ad, hk, ak, b, d = [int(x) for x in next(it).strip().split()]

    minimum_turns = 10**20

    max_debuffs_to_try = 0 if d == 0 else (ak // d + 1)
    max_buffs_to_try = 0 if b == 0 else ((hk - ad) // b + 1)
    for number_of_debuffs in range(0, max_debuffs_to_try+1):
        needed_to_cure_last_turn = False
        health_dragon = hd
        attack_dragon = ad
        health_knight = hk
        attack_knight = ak
        turns = 0

        debuffs_performed = 0
        while debuffs_performed < number_of_debuffs:
            turns += 1

            if health_dragon <= (attack_knight - d):
                if needed_to_cure_last_turn:
                    break
                else:
                    needed_to_cure_last_turn = True

                health_dragon = hd

            else:
                debuffs_performed += 1
                attack_knight -= d
                needed_to_cure_last_turn = False

            health_dragon -= attack_knight
            if health_dragon <= 0:
                break

        if debuffs_performed < number_of_debuffs or health_dragon <= 0:
            continue

        stored_dragon_health = health_dragon
        stored_knight_attack = attack_knight
        stored_turns = turns

        for number_of_buffs in range(0, 100):
            needed_to_cure_last_turn = False
            health_dragon = stored_dragon_health
            attack_dragon = ad
            health_knight = hk
            attack_knight = stored_knight_attack
            turns = stored_turns

            buffs_performed = 0
            while buffs_performed < number_of_buffs:
                turns += 1

                if health_dragon <= attack_knight:
                    if needed_to_cure_last_turn:
                        break
                    else:
                        needed_to_cure_last_turn = True

                    health_dragon = hd

                else:
                    buffs_performed += 1
                    attack_dragon += b
                    needed_to_cure_last_turn = False

                health_dragon -= attack_knight
                if health_dragon <= 0:
                    break

            if buffs_performed < number_of_buffs or health_dragon <= 0:
                continue

            while True:
                turns += 1
                if health_dragon <= attack_knight and health_knight > attack_dragon:
                    if needed_to_cure_last_turn:
                        break
                    else:
                        needed_to_cure_last_turn = True

                    health_dragon = hd

                else:
                    needed_to_cure_last_turn = False
                    health_knight -= attack_dragon
                    if health_knight <= 0:
                        minimum_turns = min(minimum_turns, turns)
                        break

                health_dragon -= attack_knight
                if health_dragon <= 0:
                    break

    answer = 'IMPOSSIBLE' if minimum_turns > 10**10 else str(minimum_turns)

    line = "Case #{0}: {1}\n".format(str(case), answer)
    output += line


with open(OUT_FILE, 'w') as fileOut:
    fileOut.write(output)
