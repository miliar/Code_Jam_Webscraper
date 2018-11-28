import sys


def cases(filename):
    with open(filename, 'r') as f:
        t = int(f.readline().strip())
        for _ in range(t):
            n = int(f.readline().strip())
            naomi = set(map(float, f.readline().strip().split()))
            ken = set(map(float, f.readline().strip().split()))
            yield (n, naomi, ken)



def solve(n, naomi, ken, epsilon=1e-7):

    def ken_choose_block(kens_blocks, chosen_naomi):
        winning_blocks = set(block for block in kens_blocks if block > chosen_naomi)
        if winning_blocks:
            optimal_block = min(winning_blocks)
        else:
            optimal_block = min(kens_blocks)
        kens_blocks.remove(optimal_block)
        return optimal_block

    def naomi_choose_block_fair(naomis_blocks):
        optimal_block = min(naomis_blocks)
        naomis_blocks.remove(optimal_block)
        return optimal_block

    def naomi_choose_block_deceitful(naomis_blocks, kens_blocks):
        max_naomi = max(naomis_blocks)
        min_naomi = min(naomis_blocks)
        max_ken = max(kens_blocks)
        min_ken = min(kens_blocks)
        if max_naomi > max_ken:
            winning_blocks = set(block for block in naomis_blocks if block > min_ken)
            optimal_block = min(winning_blocks)
            naomis_blocks.remove(optimal_block)
            return optimal_block, max_ken + epsilon
        else:
            naomis_blocks.remove(min_naomi)
            return min_naomi, max_ken - epsilon

    naomis_blocks = set(naomi)
    kens_blocks = set(ken)

    fair_score = 0
    for _ in range(n):
        chosen_naomi = naomi_choose_block_fair(naomis_blocks)
        chosen_ken = ken_choose_block(kens_blocks, chosen_naomi)
        if chosen_naomi > chosen_ken:
            fair_score += 1

    naomis_blocks = set(naomi)
    kens_blocks = set(ken)

    deceitful_score = 0
    for _ in range(n):
        chosen_naomi, told_naomi = naomi_choose_block_deceitful(naomis_blocks, kens_blocks)
        chosen_ken = ken_choose_block(kens_blocks, told_naomi)
        if chosen_naomi > chosen_ken:
            deceitful_score += 1

    return (deceitful_score, fair_score)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: {} filename'.format(sys.argv[0]))
        sys.exit(1)
    for i, case in enumerate(cases(sys.argv[1]), 1):
        print('Case #{}: {} {}'.format(i, *solve(*case)))
