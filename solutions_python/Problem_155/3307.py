lines = open("input.txt").readlines()

T = int(lines[0].strip())

def solve(people):
    total = 0
    accum = 0

    for shyness, dudes in enumerate(people):
        if dudes > 0 and accum < shyness:
            total += (shyness - accum)
            accum += (shyness - accum)
        accum += dudes

    return total

for n, line in enumerate(lines[1:]):
    max_shyness, people_str = line.strip().split(" ")
    people = [int(i) for i in list(people_str)]
    print("Case #%i: %i" % (n+1, solve(people)))
