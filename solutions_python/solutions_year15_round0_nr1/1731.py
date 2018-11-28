def solve(maxshy, people):
    extra = 0
    standing = 0
    for shyness in range(maxshy+1):
        if shyness > standing and people[shyness]:
            needed = shyness - standing
            extra += needed
            standing += needed
        standing += people[shyness]
    return extra

if __name__ == '__main__':
    cases = input()
    for case in range(cases):
        maxshy, people = raw_input().split(" ")
        maxshy = int(maxshy)
        people = map(int, list(people))
        solution = solve(maxshy, people)
        print "Case #"+str(case+1)+": "+str(solution)