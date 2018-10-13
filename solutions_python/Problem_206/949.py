import sys,os


def read_input(filename):
    f = open(filename)
    lines = f.readlines()
    curentLine = 0
    _T = int(lines[curentLine])
    for T in range(_T):
        curentLine += 1
        D, N = lines[curentLine].split()
        horses = []
        for _N in range(int(N)):
            curentLine += 1
            K, S = lines[curentLine].split()
            horses.append((int(K),int(S)))
        response = solver(int(D), int(N), horses)
        print("Case #%d: %s" % (T+1, response))
    f.close()

def solver(DISTANCE, NRCAI, horses):
    # print("Citit:", DISTANCE, NRCAI, horses)
    # gaseste calul cel mai lent
    max_ore_ramase = 0
    for K, S in horses:
        ore_ramase = (DISTANCE - K) / S
        max_ore_ramase = max(max_ore_ramase, ore_ramase)
    viteza = DISTANCE/max_ore_ramase
    return round(viteza, 6)

if len(sys.argv)>1 and sys.argv[1]:
    inputFile = sys.argv[1]
else:
    inputFile = "test_input.txt"

read_input(inputFile)
