f = open('input', 'r')
tests = int(f.readline())
for i in range(tests):
    line = f.readline().rstrip()
    bitstr, val = line.split()
    bitstr = list(bitstr)
    K = int(val)
    S = len(bitstr)
    flips = 0
    for k in range(S-K+1):
        if bitstr[k] == '-':
            flips += 1
            for j in range(k, k+K):
                if bitstr[j] == '-':
                    bitstr[j] = '+'
                else:
                    bitstr[j] = '-'
    if '-' in bitstr:
        print("Case #"+str(i+1)+": IMPOSSIBLE")
    else:
        print("Case #"+str(i+1)+": "+str(flips))


