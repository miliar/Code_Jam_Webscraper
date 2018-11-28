def parse_file(file):
    cases = []
    with open(file, 'r') as f:
        amountOfCases = f.readline()
        for line in f:
            line = line.strip()
            case = line.split(" ")
            cases.append(case)
    return cases

def removeInitialCakes(grill):
    return list("".join(grill).lstrip("+"))

def flip(cakes, k):
    matches = {'-':'+', '+':'-'}
    for i in range(k):
        cakes[i] = matches[cakes[i]]
    return cakes

def solve(grill, k):
    pancakes = list(grill)
    count = 0
    while len(pancakes) > 0 and len(pancakes) >= k:
        pancakes = removeInitialCakes(pancakes)
        if len(pancakes) >= k:
            count += 1
            pancakes = flip(pancakes, k)
    if len(pancakes) == 0:
        return count
    else:
        return "IMPOSSIBLE"

def main():
    filename = 'A-large.in'
    cases = parse_file(filename)
    outputfile = str(filename.split(".")[0]) + ".out"
    print(outputfile)
    with open(outputfile, "w") as f:
        for index in range(len(cases)):
            f.write("Case #{0}: {1}\n".format(index + 1, solve(cases[index][0], int(cases[index][1]))))
main()