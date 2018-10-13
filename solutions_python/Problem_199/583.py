def solve(test_num):
    seq, k = input().strip().split()
    k = int(k)
    seq = list(seq)

    res = 0
    for i in range(len(seq)-1, k-2, -1):
        if seq[i] == '+':
            continue
        
        res += 1
        for j in range(i-k+1, i+1):
            if seq[j] == '-':
                seq[j] = '+'
            else:
                seq[j] = '-'
    
    ok = True 
    for i in range(k):
        if seq[i] == '-':
            ok = False

    if ok:
        print("Case #{}: {}".format(test_num, res))
    else:
        print("Case #{}: IMPOSSIBLE".format(test_num))


T = int(input())

for i in range(T):
    solve(i + 1)
