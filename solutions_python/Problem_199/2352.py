from Codejam import codejam_run

@codejam_run()
def calc_min_number_of_pancake_flips(S, K):
    K = int(K)

    flip_counts = 0

    def flip(S):
        return "".join(['+' if c == '-' else '-' for c in S])

    while len(S) != 0:
        leftmost_blank_idx = S.find('-')

        if leftmost_blank_idx == -1:                # S contains only '+'
            break

        S = S[leftmost_blank_idx:]                  # crop all leftmost '+'

        if len(S) < K:                              # 0 < |S| < K
            return "IMPOSSIBLE",

        S = flip(S[:K]) + S[K:]                     # flip leftmost K pcakes
        flip_counts += 1

    return str(flip_counts),
