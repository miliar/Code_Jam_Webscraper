import sys

infile = open(sys.argv[1])
outfile = open("answer.out", "w")

def answer(case, ans):
    answer = "Case #" + str(case) + ": " + str(ans)
    print answer
    outfile.write(("\n" if case != 1 else "") + answer)

def getline():
    return infile.readline().strip("\n")

def getlist():
    num_of = int(getline())
    lst = []
    for num in range(num_of):
        lst.append(getline())
    return lst

for case in range(1, int(getline()) + 1):
    engines = set(getlist())
    queries = getlist()

    used = set()
    switches = 0
    
    for query in queries:
        used.add(query)
        if used == engines:
            switches += 1
            used = set((query,))

    answer(case, switches)