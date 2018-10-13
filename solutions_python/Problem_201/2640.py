import sys

def calculate_ls(N, stalls):
    S = [0] * (N+2)
    S[0] = 0
    S[1] = 0
    S[N+1] = 0
    i = 0
    while i < len(stalls)-1:
        #print("checking stall at %s : %s" % (i, stalls[i]))
        if stalls[i] == 1:
            S[i] = 0
            S[i+1] = 0
            i += 1
        else:
            S[i] = S[i-1] + 1 if stalls[i-1] == 0 else 0
        i += 1
    return S

def calculate_rs(N, stalls):
    S = [0] * (N+2)
    S[0] = 0
    S[N] = 0
    S[N+1] = 0
    i = len(stalls) - 1
    while i >= 1:
        if stalls[i] == 1:
            S[i] = 0
            S[i-1] = 0
            i -= 1
        else:
            S[i] = S[i+1] + 1 if stalls[i+1] == 0 else 0
        i -= 1
    return S

def calculate_minS(Ls, Rs, stalls):
    # maximize min(Ls, Rs)
    #print("min -----")
    cur_max = -sys.maxint - 1
    maxes = []
    for i in xrange(len(Ls)):
        if stalls[i] == 1:
            continue
        m = min(Ls[i], Rs[i])
        if m == cur_max:
            maxes.append(i)
        if m > cur_max:
            maxes = []
            maxes.append(i)
            cur_max = m
    #print(maxes)
    return maxes

def calculate_maxS(Ls, Rs, mins_ls_rs, stalls):
    # maximize max(Ls, Rs)
    cur_max = -sys.maxint - 1
    #print("max -----")
    maxes = []
    for i in mins_ls_rs:
        if stalls[i] == 1:
            continue
        m = max(Ls[i], Rs[i])
        if m == cur_max:
            maxes.append(i)
        if m > cur_max:
            maxes = []
            maxes.append(i)
            cur_max = m
    #print(maxes)
    return maxes

def bathroom_stalls(N, K, stalls):
    chosen = None
    while K > 0:
        #print("CUR STALLS %s" % stalls)
        Ls = calculate_ls(N, stalls)
        Rs = calculate_rs(N, stalls)
        #print("K %s Ls: %s" % (K, Ls))
        #print("K %s Rs: %s" % (K, Rs))
        mins_ls_rs = calculate_minS(Ls, Rs, stalls)
        if len(mins_ls_rs) == 1:
            stalls[mins_ls_rs[0]] = 1
            chosen = mins_ls_rs[0]
            K -= 1
            continue
        maxs_ls_rs = calculate_maxS(Ls, Rs, mins_ls_rs, stalls)
        stalls[maxs_ls_rs[0]] = 1  # either one or the leftmost one
        chosen = maxs_ls_rs[0]
        K -= 1

    return str(max(Ls[chosen], Rs[chosen])) + " " + str(min(Ls[chosen], Rs[chosen]))

def main():
    with open('/Users/alex/Downloads/C-small-1-attempt0.in.txt', 'r') as f:
        nCases = int(f.readline())
        for n in range(nCases):
            N, K = f.readline().split(" ")
            N = int(N)
            K = int(K)
            stalls = [0] * (N+2)
            stalls[0] = 1
            stalls[N+1] = 1
            result = bathroom_stalls(N, K, stalls)
            print 'Case #%s: %s' % (str(n+1), str(result))

if __name__ == '__main__':
    main()
