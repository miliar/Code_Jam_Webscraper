input_file = "D-large.in"
output_file = "deceitful_war.out"


def deceitful_war_score(n_blocks, naomi_blocks, ken_blocks):
    naomi_score = 0

    for i in range(n_blocks):
        ken_choice = ken_blocks.pop(0)

        for j in naomi_blocks:
            if j > ken_choice:
                naomi_blocks.remove(j)
                naomi_score += 1
                break
        else:  # ken's lowest block can't be beaten - we have reached the maximum amount of wins
            break

    return naomi_score



def war_score(n_blocks, naomi_blocks, ken_blocks):
    naomi_score = 0
    for i in range(n_blocks):
        naomi_choice = naomi_blocks.pop(0)

        for possible_ken_choice in ken_blocks:
            if possible_ken_choice > naomi_choice:
                ken_blocks.remove(possible_ken_choice)
                break
        else:
            ken_blocks.pop(0)
            naomi_score += 1

    return naomi_score


    

results = []
with open(input_file, 'r') as f:
    n_cases = int(f.readline())

    for i in range(n_cases):
        n_blocks = int(f.readline())

        naomi_blocks = sorted([float(i) for i in f.readline().split(' ')])
        ken_blocks = sorted([float(i) for i in f.readline().split(' ')])

        deceitful_score = deceitful_war_score(n_blocks, naomi_blocks[:], ken_blocks[:])  # create a copy so it's preserved for the war_score call
        normal_score = war_score(n_blocks, naomi_blocks[:], ken_blocks[:])

        results.append([deceitful_score, normal_score])


with open(output_file, 'w') as output:
    for i in range(len(results)):
        line = "Case #{case_number}: {deceitful_war_score} {war_score}\n".format(
            case_number=i + 1,
            deceitful_war_score=results[i][0],
            war_score=results[i][1]
        )
        output.write(line)
