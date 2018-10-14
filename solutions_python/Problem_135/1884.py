# read file and get ints
with open('A-small-attempt0.in') as fd:
    lines = fd.read().split("\n")
    if lines[-1] == "": lines = lines[:-1]
    lines = [list(map(int, line.split(" "))) for line in lines]

numCases = lines.pop(0)[0]
cases = [lines[10*i:10*i+10] for i in range(numCases)]

def chosenCard(case):
    step1, step2 = case[:5], case[5:]
    def getRow(step):
        result = step[step[0][0]]
        # print(result)
        return set(result)
    candidates = getRow(step1).intersection(getRow(step2))
    if len(candidates) == 1: return candidates.pop()
    if len(candidates) == 0: return "Volunteer cheated!"
    if len(candidates) >  1: return "Bad magician!"

for (i, case) in enumerate(cases):
    print("Case #{}: {}".format(i+1, chosenCard(case)))
