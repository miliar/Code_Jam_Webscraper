import sys


def get_war_results(naomi_blocks, ken_blocks):
    result = 0
    for n in naomi_blocks:
        bigger = [x for x in ken_blocks if x > n]
        if not bigger:
            result += 1
        else:
            ken_blocks.remove(min(bigger))
    return result


def get_deceitful_war_results(naomi_blocks, ken_blocks):
    result = 0

    for k in ken_blocks:
        if naomi_blocks[0] < k:
            del naomi_blocks[-1]
        elif naomi_blocks[0] > k:
            result += 1
            del naomi_blocks[0]

    return result


def main(argv=sys.argv):

    count = int(sys.stdin.readline())
    for i in range(count):
        sys.stdin.readline()
        naomi_blocks = sorted(map(
            float, sys.stdin.readline().split(' ')
        ), reverse=True)
        ken_blocks = sorted(map(
            float, sys.stdin.readline().split(' ')
        ), reverse=True)

        sys.stdout.write(
            'Case #{0}: {1} {2}\n'.format(
                i+1,
                get_deceitful_war_results(naomi_blocks[:], ken_blocks[:]),
                get_war_results(naomi_blocks, ken_blocks)
            )
        )
if __name__ == '__main__':
    main()
