with open('B-small-attempt0.in', 'r') as fin:
    with open('output', 'w') as fout:
        T = int(fin.readline())
        for t in range(1,T+1):
            A, B, K = [int(i) for i in fin.readline().split()]

            c = 0
            for a in range(0,A):
                for b in range(0,B):
                    if a & b < K:
                        c += 1
            
            fout.write('Case #{}: {}\n'.format(t, c))
