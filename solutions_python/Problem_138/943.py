import fileinput

__author__ = 'psmit'


def merge(N, K):
    vec = []
    while len(N) > 0 and len(K) > 0:
        if N[0] < K[0]:
            vec.append('N')
            N = N[1:]
        else:
            vec.append('K')
            K = K[1:]

    vec.extend(['N'] * len(N))
    vec.extend(['K'] * len(K))
    return vec

def is_sorted(vec):
    return all(v == 'K' for v in vec[:len(vec)//2])
def solve(vec):
    vec_copy = vec.copy()

    unfairN = 0
    while len(vec_copy) > 0:
        try:
            kindex = vec_copy.index('K')
            nindex = vec_copy.index('N', kindex)

            del vec_copy[nindex]
            del vec_copy[kindex]
            unfairN += 1
        except ValueError as e:
            break

    fairN = 0
    kcount = 0
    for v in reversed(vec):
        if v == 'K':
            kcount += 1
        else:
            if kcount == 0:
                fairN += 1
            else:
                kcount -= 1



    # while len(vec_copy) > 0 and not is_sorted(vec_copy):
    #     del vec_copy[vec_copy.index('N')]
    #     del vec_copy[len(vec_copy)-1-list(reversed(vec_copy)).index('K')]
    #
    # unfairN = len(vec_copy) // 2

    # unfairN = index = len(vec) // 2
    # while index < len(vec) and vec_copy[index] == 'N':
    #     unfairN -= 1
    #     index += 1
    return unfairN, fairN


def main():
    inp = fileinput.input()

    T = int(inp.readline())

    for t in range(1,T+1):
        inp.readline()
        N = sorted(float(x) for x in inp.readline().split())
        K = sorted(float(x) for x in inp.readline().split())

        vec = merge(N,K)
        unfair, fair = solve(vec)
        print("Case #{}: {} {}".format(t, unfair, fair))



main()
