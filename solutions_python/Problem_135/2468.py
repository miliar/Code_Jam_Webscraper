# Codejam 2014 Qualifiers - A: Magic Trick

with open("A-small-attempt0.in", "rU") as f:
    with open("A-small-attempt0.out", "w") as out:
        for currCase in range(1, int(f.readline()) + 1):
            first = int(f.readline())
            firstSet = set()
            for x in range(1, 5):
                temp = [int(x) for x in f.readline().strip().split()]
                if x == first:
                    for thing in temp:
                        firstSet.add(thing)
            second = int(f.readline())
            secondSet = set()
            for x in range(1, 5):
                temp = [int(x) for x in f.readline().strip().split()]
                if x == second:
                    for thing in temp:
                        secondSet.add(thing)
            result = firstSet.intersection(secondSet)
            if len(result) == 0:
                out.write("Case #{}: Volunteer cheated!\n".format(currCase))
            elif len(result) > 1:
                out.write("Case #{}: Bad magician!\n".format(currCase))
            else:
                assert len(result) == 1
                out.write("Case #{}: {}\n".format(currCase, result.pop()))
            
            
        
