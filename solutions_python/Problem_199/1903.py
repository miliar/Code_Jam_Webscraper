def helper(arr, ind, seq, rList):
    if seq: rList[len(seq)-1].append(seq[:])
    if ind >= len(arr): return
    for i in range(ind, len(arr)):
        seq.append(arr[i])
        helper(arr, i+1, seq, rList)
        seq.pop()

def subset(N):
    arr = range(N)
    rList = [[] for _ in range(N)]
    helper(arr, 0, [], rList)
    return rList

def flipped(comb, K, l):
    arr = [False for _ in range(l)]
    for i in comb:
        for j in range(i, i+K):
            arr[j] = not arr[j]
    return arr

def check(f, r, S, flip):
    notF = notR = False
    for i in range(len(flip)):
        stat = f[i] ^ flip[i]
        if stat != r[i]: notR = True
        if stat != f[i]: notF = True
        if notR and notF: return False
    return True

def validate(S, K):
    subsets = subset(len(S)-K+1)
    fin = [ True for _ in range(len(S))]
    rev = [ True if c == '+' else False for c in S[::-1]]
    S = [ True if c == '+' else False for c in S]
    if False not in S: return 0
    for depth in range(len(subsets)):
        for comb in subsets[depth]:
            flip = flipped(comb, K, len(S))
            if check(fin, rev, S, flip): return str(len(comb))
    return "IMPOSSIBLE"

#print(validate("+-+---", 2))

T = int(input())
for t in range(T):
    vals = input().split()
    S, K = vals[0], int(vals[1])
    print("Case #%i: %s" % (t+1, validate(S, K)))