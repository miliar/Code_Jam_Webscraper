import sys

def read_dataset(filename):
    data = open(filename)
    T = int(data.readline().strip())
    cases = []
    for i in range(0,T):
        case = data.readline().strip().split()
        row = case[0]
        S = []
        for i in range(0,len(row)):
            if row[i] == '+':
                S.append(True)
            else:
                S.append(False)
        K = int(case[1])

        cases.append([S,K])
    return T, cases

def resolve_set(dataset):
    T, cases = dataset
    flips = []
    for i in range(0,T):
        S, K = cases[i]
        flips.append(resolve(S, K))
    return flips

def resolve(S, K):
    flips = 0
    for i in range(0,len(S) - K + 1):
        if not S[i]:
            flips += 1
            for j in range(0,K):
                S[i+j] = not S[i+j]
    for i in range(0,K):
        if S[-i] == False:
            flips = -1
    return flips

def output(flips, name):
    out = name[:-3] + '.out'
    file = open(out, "w")
    for i, f in enumerate(flips):
        if f == -1:
            f = 'IMPOSSIBLE'
        file.write("Case #" + str(i+1) +": " + str(f) + "\n")

def solution():
    name = sys.argv[1]
    dataset = read_dataset(name)
    flips = resolve_set(dataset)
    output(flips, name)

solution()