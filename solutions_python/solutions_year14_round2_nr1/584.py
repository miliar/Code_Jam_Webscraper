infile = open("A-small-attempt1.in", "rU")
outfile = open("A.out", "w")

ncases = int(infile.readline())

def trim(string):
    last = ""
    output = ""

    for s in string:
        if s == last:
            continue

        output += s
        last = s        

    return output

def rep(string):
    output = []
    last = ""
    curr = []

    for s in string:
        if s == last:
            curr[1] += 1

        else:
            if curr != []:
                output.append(curr)
                
            curr = [s, 1]
            last = s

    output.append(curr)

    return output

def same(listy):
    return listy.count(listy[0]) == len(listy)

def error(listy):
    total = sum(listy)
    mean = float(total)/len(listy)

    closest_dist = abs(listy[0] - mean)
    closest = 0
    
    for i in listy:
        if abs(i - mean) <= closest_dist:
            closest = i
            closest_dist = abs(i - mean)

    err = 0

    for i in listy:
        err += abs(i - closest)

    return err

def solve(listy): # listy ascending
    moves = 0

    while not same(listy):
        listya = listy[:]
        listya[-1] -= 1

        if error(listya) > error(listy):
            return moves + error(listy)

        listy = listya
        listy.sort()
        moves += 1

    return moves
    
    
for case in xrange(1, ncases + 1):
    nstrings = int(infile.readline())

    strings = []

    for i in xrange(nstrings):
        strings.append(infile.readline().strip())

    target = trim(strings[0])
    
    for s in strings:
        if trim(s) != target:
            outfile.write("Case #%d: Fegla Won\n" % case)
            break

    else:
        reps = []

        for s in strings:
            reps.append(rep(s))

        moves = 0

        # Moves allowed: Add to 1, or add to all but one

        for i in xrange(len(reps[0])):
            listy = []

            for r in reps:
                listy.append(r[i][1])

            listy.sort()

            moves += solve(listy)

        outfile.write("Case #%d: %d\n" % (case, moves))
    
infile.close()
outfile.close()
