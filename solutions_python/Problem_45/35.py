import itertools

def getNCoins(perm, P):
    retVal = 0
    prison = [1] * P
    for p in perm:
        realP = p - 1
        prison[realP] = 0;
        tmp = realP + 1
        while tmp < P and prison[tmp] != 0:
            retVal += 1
            tmp += 1
        
        tmp = realP - 1
        while tmp >= 0 and prison[tmp] != 0:
            retVal += 1
            tmp -= 1
    
    return retVal
    

INPUT_FILE = 'inputs/C-small-attempt0.in'
OUTPUT_FILE = 'outputs/C-small-attempt0.out'

f_in = open(INPUT_FILE, 'r')
f_out = open(OUTPUT_FILE, 'w+')

N = int(f_in.readline().strip())
for i in range(N):
    P, Q = [int(x) for x in f_in.readline().strip().split()]
    pris = [int(x) for x in f_in.readline().strip().split()]
    allPerms = list(itertools.permutations(pris))
    minNCoins = Q * P;
    for perm in allPerms:
        nCoin = getNCoins(perm, P)
        if (minNCoins > nCoin):
            minNCoins = nCoin
    print("Case #" + str(i + 1) + ": " + str(minNCoins) + "\n")
    f_out.write("Case #" + str(i + 1) + ": " + str(minNCoins) + "\n")


f_in.close()
f_out.close()