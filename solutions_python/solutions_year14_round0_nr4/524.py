import sys

sys.stdin = open('warL.in', 'r')
sys.stdout = open('war.out', 'w')

def main():
    total_cases = int(input())
    for case_number in range(1, total_cases+1):
        num_blocks = int(input())
        n_blocks = list(sorted([float(i) for i in input().split()], reverse=True))
        k_blocks = list(sorted([float(i) for i in input().split()], reverse=True))
        k_wins = 0
        n_wins = 0
        k_i_regular = 0
        n_i_regular = 0
        k_i_deceit = 0
        n_i_deceit = 0
        for i in range(len(k_blocks)):
            k_regular = k_blocks[k_i_regular]
            n_regular = n_blocks[n_i_regular]
            k_deceit = k_blocks[k_i_deceit]
            n_deceit = n_blocks[n_i_deceit]

            # ken optimal
            if k_regular > n_regular:
                # burn high block
                k_wins += 1
                k_i_regular += 1
            n_i_regular += 1

            # nayomi deceit
            if n_deceit > k_deceit:
                n_wins += 1
                n_i_deceit += 1
            k_i_deceit += 1
        print('Case #%d: %d %d' % (case_number, n_wins, num_blocks-k_wins))

if __name__ == '__main__':
    main()