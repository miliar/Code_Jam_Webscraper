import random
fw = open("output.out", "w")

def getCases():
    with open("C-small-1-attempt0.in") as f:
        lines = f.read().splitlines() 
        T = int(lines[0])
        for t in range(1, T + 1):
            s = lines[t].split()
            yield {'t': t, 'N': int(s[0]), 'K': int(s[1])}

def getMyCases():
    yield {'t': 1, 's': '4 2'}
        

for T in getCases():
    N = T['N']
    K = T['K']

    s1 = int(N / 2)
    s2 = int((N-1) / 2)
    nums = [s2, s1]
    for k in range(1, K):
        n = nums.pop()
        s1 = int(n / 2)
        s2 = int((n-1) / 2)
        nums.append(s1)
        nums.append(s2)
        nums.sort()

    print ('Case #' + str(T['t']) + ': ' + str(s1) + ' ' + str(s2))
    fw.write('Case #' + str(T['t']) + ': ' + str(s1) + ' ' + str(s2) + '\n')

fw.close()
