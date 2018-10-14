__author__ = 'Antariksh Bothale'
import sys, copy

def get_War_Score(N, K):
    N = copy.deepcopy(N)
    K = copy.deepcopy(K)
    N_win = 0
    for elem in N:
        #print K
        if elem > max(K):
            K = K[1:]
            N_win += 1
        else:
            for j, k_elem in enumerate(K):
                if k_elem > elem:
                    K.pop(j)
                    break
    return N_win

def get_Deceitful_War_Score(N, K):
    N = copy.deepcopy(N)
    K = copy.deepcopy(K)
    N_win = 0
    for i, elem in enumerate(N):
        if elem < min(K):
            K.pop()
        else:
            K = K[1:]
            N_win += 1

    return N_win


if __name__ == '__main__':
    total = map(lambda x: x.strip(), sys.stdin.readlines())
    total_num = int(total[0])
    i = 1

    case_num = 0
    while (True):
        N, K = tuple([map (float, elem.split()) for elem in total[i+1:i+3]])

        i += 3
        N.sort()
        K.sort()
        #print N, K
        N_win_deceitful_war = get_Deceitful_War_Score(N, K)
        N_win_war = get_War_Score(N, K)

        case_num += 1
        print 'Case #{0}: {1} {2}'.format(case_num, N_win_deceitful_war, N_win_war)
        if case_num == total_num:
            break