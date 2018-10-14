
def print_result(i, count):
    print "Case #%d: %d" %(i+1, count)
    return

def print_impossible(i):
    print "Case #%d: IMPOSSIBLE" %(i+1)
    return

is_all_happy = lambda x: all([i == '+' for i in x])
is_all_sad = lambda x: all([i == '-' for i in x])

def flip(S, start, K):
    for zz in xrange(start, start+K):
        S[zz] = '+' if S[zz] == '-' else '-'

    return S

def process(S, K, case):
    count = 0
    i, j = 0, len(S)-1

    while True:
        # Check if its solved
        if is_all_happy(S): print_result(case, count); return
        elif is_all_sad(S):
            if len(S) % K == 0:
                print_result(case, count + (len(S) / K)); return
            print_impossible(case); return

        # Flip i
        if i != 0 and i + K - 1 > j and '+' in S[j:]:
            print_impossible(case); return

        if S[i] == '-':
            S = flip(S, i, K)
            count += 1
        i += 1

        # Check if its solved
        if is_all_happy(S): print_result(case, count); return
        elif is_all_sad(S):
            if len(S) % K == 0:
                print_result(case, count + (len(S) / K)); return
            print_impossible(case); return

        if j - K + 1 < i and '+' in S[:i]:
            print_impossible(case); return

        # Flip j
        if S[j] == '-':
            S = flip(S, j-K+1, K)
            count += 1
        j -= 1


T = int(raw_input().strip())
for i in xrange(T):
    S, K = raw_input().strip().split()
    # print S, K
    S = list(S)
    K = int(K)

    process(S, K, i)
    # print

