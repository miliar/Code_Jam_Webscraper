
input_dir = 'inputs/'
output_dir = 'outputs/'
problem = 'A'
size = 'large'

fin = open(input_dir + problem + "-" + size + '.in')
fout = open(output_dir + problem + "-" + size + '.out', "w")

T = int(fin.readline())
for t in xrange(1, T + 1):
    S, K = [st for st in fin.readline().strip().split(' ')]
    K = int(K)
    S = [c for c in S]
    count = 0
    for p in xrange(len(S)):
        if S[p] == '-':
            count += 1
            for d in xrange(K):
                if p + d >= len(S):
                    fout.write("Case #{}: {}\n".format(t, "IMPOSSIBLE"))
                    break
                S[p + d] = '+' if S[p + d] == '-' else '-'
            else:
                continue
        else:
            continue
        break
    else:
        fout.write("Case #{}: {}\n".format(t, count))
fout.close()
